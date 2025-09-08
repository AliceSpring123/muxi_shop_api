# muxi_shop_api

需要的python包:

```bash

pip install mysqlclient django-cors-headers djangorestframework

```

## apis

api:

| 模块 |描述| api | 状态 |
| ---- |---| --- |---- |
| 分类菜单 |一级分类菜单| `http://localhost:8000/menu/main_menu/` |已完成|
|分类菜单|二级分类菜单|`http://localhost:8000/menu/sub_menu?main_menu_id=1`|已完成|
|分类菜单|获取某类下的所有商品|`http://127.0.0.1:8000/goods/category/1`|已完成|
|分类菜单|获取商品详情|`http://localhost:8000/menu/sub_menu?main_menu_id=1`|已完成|
|分类菜单|二级分类菜单|`http://localhost:8000/menu/sub_menu?main_menu_id=1`|已完成|
|分类菜单|二级分类菜单|`http://localhost:8000/menu/sub_menu?main_menu_id=1`|已完成|