import json
FILE_NAME = 'cac_san_pham.json'

def load_data():
    try:
        with open(FILE_NAME,'r',encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_data(cac_san_pham):

    with open(FILE_NAME,'w',encoding='utf-8') as f:
        json.dump(cac_san_pham,f,indent=4)
def add_product(cac_san_pham):
    print("Thêm data sản phẩm mới:")
    name = input("Tên sản phẩm: ")
    brand = input("Thương hiệu: ")
    try:
        gia_ban = float(input("Giá bán: "))
        so_luong = int(input("Số lượng: "))
    except ValueError:
        print("Giá bán phải là số và số lượng phải là số nguyên.")
        return cac_san_pham
    max_id_num = 0
    for p in cac_san_pham:
        try:
            id_num = int(p['id'][1:])
            if id_num > max_id_num:
                max_id_num = id_num
        except (ValueError, KeyError):
            continue
    new_id = f"P{max_id_num + 1:03d}"
    new_product = {
        "id": new_id,
        "ten": name,
        "brand": brand,
        "gia": gia_ban,
        "sl": so_luong
    }
    cac_san_pham.append(new_product)
    print("Đã thêm sản phẩm thành công.")
    return cac_san_pham