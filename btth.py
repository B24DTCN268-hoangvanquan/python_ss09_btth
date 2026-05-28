branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", 
                "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]

while True:
        choice = int(input("""
===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4): """))
        
        match choice:
            case 1:
                print("\n--- BÁO CÁO DOANH THU ---")

                for i in range(len(branch_names)):

                    if target_achieved[i] == True:
                        status = "Đạt"
                    else:
                        status = "Không Đạt"

                    print(f"Chi nhánh: {branch_names[i]}")
                    print(f"Doanh thu: {daily_revenues[i]:,} VNĐ")
                    print(f"Trạng thái: {status}")
                    print("-" * 40)

                print(f"Tổng doanh thu: {sum(daily_revenues):,} VNĐ\n")
            case 2:
                max_rev = max(daily_revenues)
                min_rev = min(daily_revenues)
                max_index = daily_revenues.index(max_rev)
                min_index = daily_revenues.index(min_rev)
                print("\n--- THỐNG KÊ ---")
                print(f"Chi nhánh doanh thu CAO NHẤT: {branch_names[max_index]} ({max_rev:,} VNĐ)")
                print(f"Chi nhánh doanh thu THẤP NHẤT: {branch_names[min_index]} ({min_rev:,} VNĐ)\n")

            case 3:
                failed_branches = []
                for i in range(len(branch_names)):
                    if not target_achieved[i]:
                        failed_branches.append(branch_names[i])
                print("\n--- DANH SÁCH CƠ SỞ KHÔNG ĐẠT ---")
                print(failed_branches, "\n")
            case 4:
                print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
                break
            case _:
                print("\n[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!\n")

