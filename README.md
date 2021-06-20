# Chatbot
#.( +++++ Yêu cầu thư mục này phải nằm trong đường dẫn localhosst  +++++)
	+ Đặt trong đường dẫn của locahost.
	+ File database sử dụng là data_trees_chatbot.sql để import vào csdl.Để chatbot lẫn website sử dụng.
	+ Tên csdl đặt là data_trees.
#Thư mục chatbot chứa source code của Bot:
	=> Để sử dụng được bot: ( Các terminal đều ở đường dẫn chứa chatbot : ví dụ : D:/rasa/chatbot ) or [ có thể dùng ( cài đặt môi trường ảo anaconda - Tốn time và cần cài anaconda " Ở python của máy đã có thể chạy chatbot , nếu không run được thầy liên hệ em ạ " )]
	+ Cài đặt rasa trong môi trường python: pip install rasa
	+ Cài đặt các thư viện cần thiết: pip install feedparser , pip install mysql-connector-python (nếu sai có thể gg).
	+ Cài đặt các gói nếu còn thiếu ...
	 => Sau khi cài đặt, cần chạy 2 terminal song song : 
   1 . chạy sever API: rasa run --model models --enable-api --cors "*"
	 2. chạy actions : rasa run actions 
	=> Cần bật xampp lên ...Apache và MySQL để truy xuất dữ liệu.
#Khi đó API gọi đến đã được chạy. => Chạy file index.html trong chatbot để test nhanh.
					=> Mở localhost => NLNComputerSciense giao diện web kèm chatbot hoàn chỉnh.
						=> Nội dung chat trong file NLU. 
					Ví dụ: User: Hi
						Bot: ........
						User: Anh tên Thành Công
						Bot: .....
						User: Bạn có thể làm gì?
						Bot: .....
						User: Các cây trồng thuộc loại thân gỗ?
						Bot: ..........
						User: Cây trồng ở khu vực Đồng bằng sông Hồng và có công dụng cải tạo đất
						............
