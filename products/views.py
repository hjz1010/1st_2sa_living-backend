from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q

from products.models import Category, SubCategory, Product

class CategoryView(View):
    def get(self, request):
        category_list     = [{
            'id': category.id, 
            'name': category.name
            } for category in Category.objects.all()]

        sub_category_list = [{
            'id': subcategory.id, 
            'name': subcategory.name, 
            'category': subcategory.category.id
            } for subcategory in SubCategory.objects.all()]

        return JsonResponse({'message': 'SUCCESS', 'category_list': category_list,'sub_category_list': sub_category_list}, status=200)


class ProductListView(View):
    def get(self, request):
        try:
            DEFAULT_LIMIT = 4
            DEFAULT_OFFSET = 0
            PRICE_RANGE = [0, 100000, 500000, 1000000]

            category_id     = request.GET.get('category_id', None)
            sub_category_id = request.GET.get('sub_category_id', None)
            limit           = int(request.GET.get('limit', DEFAULT_LIMIT))
            offset          = request.GET.get('offset', DEFAULT_OFFSET))
            sort_type       = request.GET.get('sort_type', 'id')

            color_name  = request.GET.get('color')
            brand_id    = request.GET.get('brand_id')
            price_range = request.GET.get('price_range', None)
            # 1: 10만원 이하,  2: 50만원 이하,  3: 100만원이하

            q = Q()

            if category_id:
                category = Category.objects.get(id = category_id)
                q       &= Q(sub_category__category = category)

            if sub_category_id:
                sub_category = SubCategory.objects.get(id = sub_category_id)
                q           &= Q(sub_category = sub_category)

            if color_name:
                color = Color.objects.get(english_name=color_name)
                q    &= Q(color=color)

            if brand_id:
                brand = Brand.objects.get(id=brand_id)
                q    &= Q(furniture__brand=brand)
            
            if price_range:
                q &= Q(price__lte = PRICE_RANGE[int(price_range)])

            count = Product.objects.filter(q).count()   

            product = Product.objects.annotate(total_quantity=Sum(F('orderitem__quantity')))

            sort_set = { 
                'id'           : 'id',
                'new'          : 'furniture__updated_at',
                'high_price'   : '-price',
                'low_price'    : 'price',
                'sale_quantity': 'total_quantity'
            }

            sort_field = sort_set.get(sort_type, 'id')       

            products = product.filter(q).order_by(sort_field)[offset:offset+limit]

            product_list = [{
                'id'         : product.id,
                'image'      : product.thumbnail_image_url,
                'brandName'  : product.furniture.brand.name,  
                'productName': product.furniture.korean_name + '_' + product.color.korean_name,
                'price'      : product.price
            } for product in products]                

            return JsonResponse({'message': 'SUCCESS', 'count': count, 'product_list': product_list}, status=200)
        except Category.DoesNotExist:
            return JsonResponse({'message': 'INVALID_CATEGORY'}, status=404)
        except SubCategory.DoesNotExist:   
            return JsonResponse({'message': 'INVALID_SUBCATEGORY'}, status=404)    
     

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product          = Product.objects.get(id=product_id)
            related_products = Product.objects.filter(furniture_id=product.furniture_id)

            result = [{
                    'english_name'         : product.furniture.english_name + '_' + product.color.english_name,
                    'korean_name'          : product.furniture.korean_name + '_' + product.color.korean_name,
                    'main_image'           : product.main_image_url,
                    'detail_image'         : [image.image_url for image in product.detail_image.all()],
                    'price'                : product.price,
                    'brand'                : product.furniture.brand.name,                    
                    'related_products_list': [{
                        'id'   : related_product.id,
                        'color': related_product.color.english_name,
                        'price': related_product.price
                    } for related_product in related_products]
                }]
            return JsonResponse({'result': result}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'INVALID_PRODUCT_ID'}, status=404)
        
