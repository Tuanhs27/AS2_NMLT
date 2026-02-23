import product_manager as pm
#Viết hàm funtion để chạy giao diện
def main():
    cac_san_pham = pm.load_data()
    while True:
        print("\nMenu:")
        print("1. Thêm sản phẩm mới")
        print("2. Cập nhật sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Hiển thị tất cả sản phẩm")
        print("6. Thoát")
        choice = input("Chọn một tùy chọn: ")
        if choice == '1':
            cac_san_pham = pm.add_product(cac_san_pham)
            pm.save_data(cac_san_pham)
        elif choice == '2':
            cac_san_pham = pm.cap_nhat_san_pham(cac_san_pham)
            pm.save_data(cac_san_pham)
        elif choice == '3':
            cac_san_pham = pm.xoa_san_pham(cac_san_pham)
            pm.save_data(cac_san_pham)
        elif choice == '4':
            pm.tim_san_pham(cac_san_pham)
        elif choice == '5':
            pm.hien_thi_san_pham(cac_san_pham)
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
main()
