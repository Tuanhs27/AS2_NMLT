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
#hàm thêm sản phẩm
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
#hàm cập nhật sản phẩm
def cap_nhat_san_pham(cac_san_pham):

    print("Cap nhật sản phẩm:")
    sp_id = input("Nhập ID sản phẩm cần cập nhật: ").strip().upper()
    for p in cac_san_pham:
        if p['id'] == sp_id:
            print(f"Sản phẩm hiện tại: {p}")
            name = input("Tên sản phẩm mới (để trống nếu không đổi): ")
            brand = input("Thương hiệu mới (để trống nếu không đổi): ")
            gia_ban_input = input("Giá bán mới (để trống nếu không đổi): ")
            so_luong_input = input("Số lượng mới (để trống nếu không đổi): ")
            if name:
                p['ten'] = name
            if brand:
                p['brand'] = brand
            if gia_ban_input:
                try:
                    p['gia'] = float(gia_ban_input)
                except ValueError:
                    print("Giá bán phải là số. Cập nhật giá bán bị bỏ qua.")
            if so_luong_input:
                try:
                    p['sl'] = int(so_luong_input)
                except ValueError:
                    print("Số lượng phải là số nguyên. Cập nhật số lượng bị bỏ qua.")
            print("Đã cập nhật sản phẩm thành công.")
            return cac_san_pham
    print("Không tìm thấy sản phẩm với ID đã cho.")
    return cac_san_pham
def xoa_san_pham(cac_san_pham):
    print("Xóa sản phẩm:")
    sp_id = input("Nhập ID sản phẩm cần xóa: ").strip().upper()
    for p in cac_san_pham:
        if p['id'] == sp_id:
            cac_san_pham.remove(p)
            print("Đã xóa sản phẩm thành công.")
            return cac_san_pham
    print("Không tìm thấy sản phẩm với ID đã cho.")
    return cac_san_pham
def tim_san_pham(cac_san_pham):
    print("Tìm kiếm sản phẩm:")
    sp_ten = input("Nhập tên sản phẩm cần tìm: ").strip().lower()
    ket_qua = []
    for p in cac_san_pham:
        if sp_ten in p['ten'].lower():
            ket_qua.append(p)
    if ket_qua:
        print("Kết quả tìm kiếm:")
        for sp in ket_qua:
            print(sp)
    else:
        print("Không tìm thấy sản phẩm nào phù hợp.")
def hien_thi_san_pham(cac_san_pham):
    print("Danh sách sản phẩm:")
    for p in cac_san_pham:
        print(p)
