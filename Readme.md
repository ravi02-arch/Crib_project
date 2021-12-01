INTRODUCTION

- This project is a supermarket billing APP
- It is subdivided into categories, subcategories & items
- The django APP name is billing 
- The APP has been made with models, rest-framework and on Postgresql database
- The APP is hosted on cloud server, it can be accessed by below end-points

eg: - API END POINT(GET)
	- http://3.7.213.105:8000/item/view        ---->Method[GET]

	- http://3.7.213.105:8000/item/view?category=Food  ---->Method[GET]

	- http://3.7.213.105:8000/item/view?subcategory=Beverage  ---->Method[GET]

	- http://3.7.213.105:8000/item/view?item=Shirt  ---->Method[GET]
	
	- http://3.7.213.105:8000/item/create   ---->Method[POST] -> form_data eg:- {'name': 'Soda', 'amount':40, 'subcategory':'Beverage'}

	- http://3.7.213.105:8000/item/update/<str:item_name>   ---->Method[PUT] ->  form_data eg:- {'name': 'Shirt', 'amount':700, 'subcategory':'Male'}

	- http://3.7.213.105:8000/item/delete/<str:item_name>   ---->Method[DELETE]
 
APP STRUCTURE
 
  - django-app -> supermarket/billing
  - django-project -> supermarket/