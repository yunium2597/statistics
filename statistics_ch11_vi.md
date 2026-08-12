# 11 

## Sai số R.M.S. cho Hồi quy (The R.M.S. Error for Regression)

_Đó là những hệ quả toán học chính thức của tương quan chuẩn. Nhiều dữ liệu sinh trắc học chắc chắn cho thấy sự thống nhất chung với các đặc điểm được mong đợi dựa trên giả định này: mặc dù tôi không rõ liệu vấn đề này đã được đưa ra để tiến hành bất kỳ cuộc nghiên cứu đánh giá nào đủ khắt khe hay chưa. Sự thống nhất ở mức xấp xỉ có lẽ là tất cả những gì cần thiết để biện minh cho việc sử dụng tương quan như một đại lượng mô tả quần thể; hiệu quả của nó ở khía cạnh này là không thể nghi ngờ, và không loại trừ khả năng trong một số trường hợp, cùng với các giá trị trung bình và phương sai, nó cung cấp một sự mô tả hoàn chỉnh về sự biến thiên đồng thời của các biến số._ 

—SIR R. A. FISHER (ANH, 1890–1962)<sup>1</sup> 

#### 1. GIỚI THIỆU

Phương pháp hồi quy có thể được sử dụng để dự báo _y_ từ _x_. Tuy nhiên, các giá trị thực tế thường khác với các dự báo. Khác biệt bao nhiêu? Mục tiêu của phần này là đo lường mức độ tổng thể của những sự khác biệt đó bằng cách sử dụng sai số r.m.s. (root-mean-square error - sai số căn quân phương). Ví dụ, hãy xem xét chiều cao và cân nặng của 471 người đàn ông từ 18–24 tuổi trong mẫu HANES5 (phần 1 của chương 10). Các thống kê tóm tắt là: 

chiều cao trung bình ≈ 70 inch, SD ≈ 3 inch; cân nặng trung bình ≈ 180 pound, SD ≈ 45 pound, _r_ ≈ 0.40 

Tóm tắt lại một cách ngắn gọn, khi biết chiều cao của một người đàn ông, cân nặng của anh ta được dự báo bởi cân nặng trung bình của tất cả những người đàn ông có cùng chiều cao đó. Mức trung bình này có thể được ước lượng bằng phương pháp hồi quy. Hình 1 biểu diễn đường hồi quy. Người A trên biểu đồ cao khoảng 72 inch. Ước lượng hồi quy cho cân nặng trung bình ở chiều cao này là 

Hình 1. Các sai số dự báo (Prediction errors). Sai số là khoảng cách ở phía trên (+) hoặc phía dưới (-) đường hồi quy. Biểu đồ phân tán (scatter diagram) thể hiện chiều cao và cân nặng của 471 người đàn ông từ 18–24 tuổi trong mẫu HANES5. 

![](images/stat_ch11.pdf-0002-02.png)

192 pound (phần 1 của chương 10). Tuy nhiên, cân nặng thực tế của A là 456 pound. Dự báo bị lệch đi 264 pound: 

sai số = cân nặng thực tế − cân nặng dự báo = 456 lb − 192 lb = 264 lb. 

Trong biểu đồ, sai số dự báo là khoảng cách thẳng đứng của A ở phía trên đường hồi quy. 

Người C trên biểu đồ cao 80,5 inch và nặng 183 pound. Đường hồi quy dự báo cân nặng của anh ta là 243 pound. Vì vậy, có một sai số dự báo là 183 lb − 243 lb = −60 lb. Trong biểu đồ, sai số này được biểu thị bằng khoảng cách thẳng đứng của C ở phía dưới đường hồi quy. 

![](images/stat_ch11.pdf-0002-07.png)

![](images/stat_ch11.pdf-0002-08.png)

![](images/stat_ch11.pdf-0002-09.png)

− Khoảng cách của một điểm ở phía trên (+) hoặc phía dưới (-) đường hồi quy là sai số = thực tế − dự báo (error = actual − predicted). 

![](images/stat_ch11.pdf-0002-11.png)

Hình 2. Sai số dự báo bằng khoảng cách thẳng đứng tính từ đường hồi quy. 

![](images/stat_ch11.pdf-0003-03.png)

Hình 2 cho thấy mối liên hệ giữa các sai số dự báo và các khoảng cách tính từ đường hồi quy. Mức độ tổng thể của các sai số này được đo lường bằng cách lấy giá trị căn quân phương (root-mean-square) của chúng (trang 66). Kết quả thu được gọi là _sai số r.m.s. của đường hồi quy_ (r.m.s. error of the regression line). 

Quay lại Hình 1. Mỗi điểm trong số 471 điểm trên biểu đồ phân tán nằm ở một khoảng cách thẳng đứng nào đó phía trên hoặc phía dưới đường hồi quy, tương ứng với một sai số dự báo tạo ra bởi đường thẳng này. Sai số r.m.s. của đường hồi quy khi dự báo cân nặng từ chiều cao là 

![](images/stat_ch11.pdf-0003-06.png)

Điều này trông có vẻ phức tạp, nhưng kết quả tính toán là khoảng 41 pound. (Một cách tính nhẩm nhanh hơn sẽ được trình bày trong phần tiếp theo.) 

Sai số r.m.s. có một ý nghĩa về mặt đồ họa: một điểm điển hình trong Hình 1 nằm ở phía trên hoặc phía dưới đường hồi quy một khoảng chừng 41 pound. Do đường thẳng này dùng để dự báo cân nặng dựa trên chiều cao, chúng ta có thể kết luận rằng đối với những người đàn ông điển hình trong nghiên cứu, cân nặng thực tế chênh lệch so với cân nặng dự báo khoảng chừng 41 pound. 

![](images/stat_ch11.pdf-0003-09.png)

Sai số r.m.s. cho hồi quy cho biết các điểm điển hình nằm cách đường hồi quy bao xa về phía trên hoặc phía dưới. 

![](images/stat_ch11.pdf-0003-11.png)

Vai trò của sai số r.m.s. đối với đường hồi quy cũng giống như vai trò của độ lệch chuẩn (SD) đối với giá trị trung bình. Chẳng hạn, khoảng 68% các điểm trên biểu đồ phân tán sẽ nằm trong khoảng một sai số r.m.s. so với đường hồi quy; khoảng 95% trong số đó sẽ nằm trong khoảng hai sai số r.m.s. Quy tắc kinh nghiệm (rule of thumb) này đúng với nhiều tập dữ liệu, nhưng không phải là tất cả; nó được minh họa trong Hình 3. 

Vậy đối với dữ liệu chiều cao-cân nặng thì sao? Máy tính nhận thấy các dự báo là chính xác trong phạm vi một sai số r.m.s. (41 pound) cho 340 trên tổng số 471 người đàn ông, chiếm tỷ lệ 72%. Quy tắc kinh nghiệm này hoàn toàn không tệ chút nào. Các dự báo là chính xác 

Hình 3. Quy tắc kinh nghiệm. Khoảng 68% các điểm trên biểu đồ phân tán rơi vào bên trong dải có các cạnh song song với đường hồi quy, và cách đường này một khoảng bằng một sai số r.m.s. (lên hoặc xuống). Khoảng 95% các điểm nằm trong dải rộng hơn có các cạnh song song với đường hồi quy, và cách một khoảng bằng hai lần sai số r.m.s. 

![](images/stat_ch11.pdf-0004-02.png)

trong phạm vi hai sai số r.m.s. (82 pound) cho 451 trên 471 người đàn ông, tương đương 96%. Kết quả này thậm chí còn phù hợp hơn với quy tắc kinh nghiệm. 

Tiếp theo, chúng ta sẽ so sánh sai số r.m.s. của hồi quy với sai số r.m.s. của một phương pháp dự báo cơ sở (baseline prediction method). Phương pháp cơ sở chỉ đơn giản bỏ qua các giá trị _x_ và sử dụng giá trị trung bình của _y_ để dự báo _y_. Với phương pháp này, các dự báo sẽ nằm trên một đường ngang đi qua giá trị trung bình của _y_. 

![](images/stat_ch11.pdf-0004-05.png)

Về mặt đồ họa, các sai số dự báo cho phương pháp thứ hai là các khoảng cách thẳng đứng ở phía trên và phía dưới đường ngang này, như được thể hiện trên hình phác thảo. Về mặt tính toán, các sai số này chính là các độ lệch (deviations) so với giá trị trung bình của _y_. Do đó, sai số r.m.s. cho phương pháp thứ hai chính là độ lệch chuẩn (SD) của _y_: hãy nhớ rằng, độ lệch chuẩn (SD) là giá trị r.m.s. của các độ lệch so với mức trung bình. 

![](images/stat_ch11.pdf-0004-07.png)

![](images/stat_ch11.pdf-0004-08.png)

![](images/stat_ch11.pdf-0004-09.png)

Độ lệch chuẩn (SD) của _y_ cho biết các điểm điển hình nằm cách đường ngang đi qua trung bình của _y_ bao xa về phía trên hoặc phía dưới. Nói cách khác, SD của _y_ chính là sai số r.m.s. cho phương pháp cơ sở — dự báo _y_ bằng giá trị trung bình của nó, và hoàn toàn bỏ qua các giá trị _x_. 

![](images/stat_ch11.pdf-0004-11.png)

### Bài tập Phần A 

1. Hãy quan sát Hình 1, sau đó điền vào chỗ trống: người B là ______ và ______, trong khi D là ______ và ______. Lựa chọn: thấp (short), cao (tall), gầy (skinny), mập (chubby). 

2. Hãy quan sát Hình 1, sau đó cho biết mỗi phát biểu sau đây là đúng hay sai: 

   - (a) E có cân nặng trên mức trung bình. 
   - (b) E có cân nặng trên mức trung bình, so với những người đàn ông có cùng chiều cao. 

3. Một đường hồi quy được khớp (fitted) với một tập dữ liệu nhỏ. Đối với mỗi đối tượng, bảng dưới đây thể hiện giá trị thực tế của _y_ và giá trị dự báo từ đường hồi quy. (Giá trị của _x_ không được hiển thị). Hãy tính các sai số dự báo, và sai số r.m.s. của đường hồi quy. 

| Giá trị thực tế của _y_ (_Actual_) | Giá trị dự báo của _y_ (_Predicted_) |
|---|---|
| 57 | 64 |
| 63 | 62 |
| 43 | 40 |
| 51 | 52 |
| 49 | 45 |

![](images/stat_ch11.pdf-0005-09.png)

4. Dưới đây là ba biểu đồ phân tán. Đường hồi quy đã được vẽ qua từng biểu đồ bằng cách ước lượng bằng mắt. Trong mỗi trường hợp, hãy đoán xem sai số r.m.s. là 0.2, hay 1, hay 5. 

![](images/stat_ch11.pdf-0005-11.png)

5. Một đường hồi quy để dự báo thu nhập có sai số r.m.s. là \$2.000. Nó dự báo thu nhập của một người là \$20.000. Dự báo này có thể chính xác với mức chênh lệch (give or take) là: vài trăm đô la, vài nghìn đô la, hay mười hoặc hai mươi nghìn đô la. 

6. Một cán bộ tuyển sinh đang cân nhắc lựa chọn giữa hai phương pháp dự báo điểm số năm nhất. Phương pháp thứ nhất có sai số r.m.s. là 12. Phương pháp còn lại có sai số r.m.s. là 7. Trong điều kiện các yếu tố khác đều như nhau, ông ấy nên chọn phương pháp nào? Tại sao? 

7. Một đường hồi quy dùng để dự báo điểm kiểm tra có sai số r.m.s. là 8 điểm. 

   - (a) Khoảng 68% số trường hợp, các dự báo sẽ chính xác trong phạm vi ______ điểm. 
   - (b) Khoảng 95% số trường hợp, các dự báo sẽ chính xác trong phạm vi ______ điểm. 

8. Biểu đồ phân tán ở trang tiếp theo cho thấy thu nhập của một mẫu gồm 168 cặp vợ chồng đang đi làm ở Louisiana. Các thống kê tóm tắt như sau: 
   - thu nhập trung bình của chồng = \$45.000, SD = \$25.000; thu nhập trung bình của vợ = \$28.000, SD = \$20.000 

   - (a) Nếu bạn dự báo thu nhập của người vợ là \$28.000 và bỏ qua thu nhập của người chồng, thì sai số r.m.s. của bạn sẽ là ______. 
   - (b) Tất cả các dự báo đều nằm trên một trong những đường thẳng trên biểu đồ. Đó là đường nào? Hãy giải thích câu trả lời của bạn. 

![](images/stat_ch11.pdf-0006-02.png)

_Đáp án cho các bài tập này nằm ở các trang A63–64._ 

#### 2. TÍNH TOÁN SAI SỐ R.M.S. 

Sai số r.m.s. cho đường hồi quy đo lường các khoảng cách ở phía trên hoặc phía dưới đường hồi quy (phần bên trái của Hình 4). Phần bên phải của Hình 4 cho thấy một đường thẳng khác, đó là đường ngang đi qua trung bình của _y_. Sai số r.m.s. cho đường thẳng đó chính là độ lệch chuẩn (SD) của _y_, như đã thảo luận ở trang 183. 

Hình 4. Sai số r.m.s. của đường hồi quy, và độ lệch chuẩn (SD) của _y_. 

![](images/stat_ch11.pdf-0006-07.png)

Sai số r.m.s. (căn quân phương) của đường hồi quy sẽ nhỏ hơn độ lệch chuẩn (SD) của _y_, bởi vì đường hồi quy nằm gần các điểm hơn so với đường nằm ngang. Sai số r.m.s. sẽ nhỏ hơn theo hệ số 1 − _r_<sup>2</sup> . 

![](images/stat_ch11.pdf-0007-01.png)

![](images/stat_ch11.pdf-0007-02.png)

![](images/stat_ch11.pdf-0007-03.png)

Sai số r.m.s. của đường hồi quy của _y_ theo _x_ có thể được tính bằng 1 − _r_<sup>2</sup> × độ lệch chuẩn (SD) của _y_ . 

![](images/stat_ch11.pdf-0007-05.png)

Cần đưa độ lệch chuẩn (SD) nào vào công thức? Đó là SD của biến số đang được dự báo. Nếu bạn đang dự báo cân nặng từ chiều cao, hãy sử dụng SD của cân nặng. Sai số r.m.s. phải có đơn vị là pound, chứ không phải inch. Nếu bạn đang dự báo thu nhập từ giáo dục, hãy sử dụng SD của thu nhập. Sai số r.m.s. phải có đơn vị là đô la, chứ không phải năm. 

![](images/stat_ch11.pdf-0007-07.png)

Đơn vị của sai số r.m.s. giống với đơn vị của biến số đang được dự báo. 

![](images/stat_ch11.pdf-0007-09.png)

Trong biểu đồ phân tán (scatter diagram) về chiều cao - cân nặng (Hình 1), có 471 sai số dự báo, tương ứng cho mỗi người đàn ông. Việc tìm giá trị trung bình toàn phương (root-mean-square) của 471 sai số này có vẻ tốn rất nhiều công sức. Nhưng hệ số 1 − _r_<sup>2</sup> cung cấp cho bạn một lối tắt trong việc tính toán. Sai số r.m.s. của đường hồi quy để dự báo cân nặng từ chiều cao bằng 

![](images/stat_ch11.pdf-0007-11.png)

Sai số r.m.s. không nhỏ hơn nhiều so với độ lệch chuẩn (SD) của cân nặng, vì cân nặng không có tương quan quá chặt chẽ với chiều cao: _r_ ≈ 0 . 40. Việc biết chiều cao của một người đàn ông không giúp ích nhiều trong việc dự báo cân nặng của người đó. 

Công thức này khó chứng minh nếu không sử dụng đại số. Nhưng có ba trường hợp đặc biệt rất dễ thấy. Đầu tiên, giả sử _r_ = 1. Khi đó, tất cả các điểm nằm trên một đường thẳng có hệ số góc dương (hướng lên). Đường hồi quy đi qua tất cả các điểm trên biểu đồ phân tán, và tất cả các sai số dự báo đều bằng 0. Vì vậy, sai số r.m.s. phải bằng 0. Và đó chính xác là những gì công thức thể hiện. Hệ số này được tính ra là 

![](images/stat_ch11.pdf-0007-14.png)

Trường hợp _r_ = −1 cũng tương tự, ngoại trừ việc đường thẳng đi xuống. Sai số r.m.s. vẫn bằng 0, và hệ số là 

![](images/stat_ch11.pdf-0007-16.png)

Trường hợp thứ ba là _r_ = 0. Khi đó không có mối quan hệ tuyến tính nào giữa các biến số. Vì vậy, đường hồi quy không giúp ích trong việc dự báo _y_ , và sai số r.m.s. của nó phải bằng độ lệch chuẩn (SD). Hệ số lúc này là 

![](images/stat_ch11.pdf-0007-18.png)

Sai số r.m.s. đo lường mức độ phân tán xung quanh đường hồi quy theo giá trị tuyệt đối: pound, đô la, v.v. Mặt khác, hệ số tương quan (correlation coefficient) đo lường sự phân tán tương đối so với độ lệch chuẩn (SD), và không có đơn vị. Sai số r.m.s. liên kết với độ lệch chuẩn (SD) thông qua hệ số tương quan. Đây là lần thứ ba _r_ xuất hiện trong câu chuyện này. 

- _r_ mô tả mức độ tập trung của các điểm xung quanh một đường thẳng, tương đối so với các độ lệch chuẩn (SD) (Chương 8). 

- _r_ cho biết giá trị trung bình của _y_ phụ thuộc vào _x_ như thế nào—tương ứng với mỗi mức tăng một SD của _x_ thì trung bình chỉ có mức tăng _r_ SD trong _y_ (Chương 10). 

- _r_ quyết định độ chính xác của các dự báo hồi quy, thông qua công thức tính sai số r.m.s. 

_Một lưu ý thận trọng._ Nếu bạn ngoại suy (extrapolate) vượt ra ngoài phạm vi dữ liệu, hoặc sử dụng đường thẳng để đưa ra ước lượng cho những người khác biệt so với các đối tượng trong nghiên cứu, sai số r.m.s. không thể cho bạn biết khả năng sai lệch là bao nhiêu. Điều đó nằm ngoài sức mạnh của toán học. 

### Bài tập Phần B 

1. Một trường luật tìm thấy mối quan hệ sau đây giữa điểm thi LSAT và điểm năm thứ nhất: 

điểm LSAT trung bình = 165, SD = 5
điểm năm thứ nhất trung bình = 65, SD = 10, _r_ = 0 . 6

Cán bộ tuyển sinh sử dụng đường hồi quy để dự báo điểm năm thứ nhất từ điểm LSAT. Sai số r.m.s. của đường thẳng là bao nhiêu? Các lựa chọn: 5, 10, 1 − 0 . 6<sup>2</sup> × 5, 1 − 0 . 6<sup>2</sup> × 10 

2. (Tiếp tục Bài tập 1.) 

![](images/stat_ch11.pdf-0008-10.png)

   - (c) Lặp lại phần (a) và (b), nếu bạn được phép sử dụng điểm LSAT của sinh viên này. 

3. Tại một trường đại học nọ, điểm trung bình GPA năm nhất trung bình khoảng 3.0, với SD khoảng 0.5; chúng có tương quan khoảng 0.6 với GPA trung học. Người A dự báo GPA năm nhất chỉ dựa vào giá trị trung bình. Người B dự báo GPA năm nhất bằng phương pháp hồi quy, sử dụng GPA trung học. Người nào có sai số r.m.s. nhỏ hơn? Nhỏ hơn bao nhiêu lần (hệ số là bao nhiêu)? 

_Đáp án cho các bài tập này có ở trang A64._ 

#### 3. VẼ BIỂU ĐỒ CÁC PHẦN DƯ (RESIDUALS) 

Các sai số dự báo thường được gọi là _phần dư_ (residuals). Các nhà thống kê khuyên bạn nên vẽ đồ thị các phần dư. Phương pháp này được chỉ ra trong Hình 5 ở trang sau. Mỗi điểm trên biểu đồ phân tán được chuyển sang một biểu đồ thứ hai, gọi là _biểu đồ phần dư_ (residual plot), theo cách như sau: Tọa độ _x_ được giữ nguyên. Nhưng tọa độ _y_ được thay thế bằng phần dư tại điểm đó—tức là khoảng cách nằm trên (+) hoặc dưới (−) 

Hình 5. Vẽ đồ thị phần dư. 

![](images/stat_ch11.pdf-0009-03.png)

so với đường hồi quy. Hình 6 hiển thị biểu đồ phần dư cho biểu đồ phân tán chiều cao - cân nặng của Hình 1. Hình 5 và Hình 6 gợi ý rằng các phần dư dương cân bằng với các phần dư âm. Về mặt toán học, trung bình của các phần dư từ đường hồi quy phải bằng 0. Các hình ảnh này cũng cho thấy một điều khác. Khi bạn nhìn qua biểu đồ phần dư, không có xu hướng hệ thống nào cho thấy các điểm trôi lên (hoặc xuống). Về cơ bản, lý do là vì toàn bộ xu hướng đi lên hay đi xuống đã được loại bỏ khỏi các phần dư, và đã được hấp thụ vào đường hồi quy. 

![](images/stat_ch11.pdf-0009-05.png)

Trung bình của các phần dư bằng 0; và đường hồi quy cho biểu đồ phần dư nằm ngang. 

![](images/stat_ch11.pdf-0009-07.png)

Hình 6. Một biểu đồ phần dư. Biểu đồ phân tán ở bên trái hiển thị chiều cao và cân nặng của 471 người đàn ông từ 18–24 tuổi trong mẫu HANES5, kèm theo đường hồi quy. Biểu đồ phần dư được hiển thị ở bên phải. Không có xu hướng hay mô hình (pattern) nào trong các phần dư. 

![](images/stat_ch11.pdf-0009-09.png)

Biểu đồ phần dư ở Hình 6 không cho thấy mô hình nào. Để so sánh, Hình 7 hiển thị một biểu đồ phần dư (đối với dữ liệu giả định) với một mô hình rõ rệt. Với kiểu mô hình này, việc sử dụng đường hồi quy rất có thể là một sai lầm. Thường thì, bạn có thể phát hiện các đặc điểm phi tuyến (non-linearities) bằng cách nhìn vào biểu đồ phân tán. Tuy nhiên, biểu đồ phần dư có thể mang lại một bài kiểm tra nhạy bén hơn—bởi vì thang đo trục dọc có thể được phóng to đủ để xem xét kỹ lưỡng mọi thứ. Các biểu đồ phần dư là công cụ chẩn đoán (diagnostics) hữu ích trong _hồi quy bội_ (multiple regression); ví dụ, khi dự báo GPA năm nhất từ điểm SAT và GPA trung học.<sup>2</sup> (Hồi quy bội được thảo luận trong phần 3 của Chương 12.) 

Hình 7. Biểu đồ phần dư với một mô hình rõ rệt. Rất có thể việc khớp (fit) đường hồi quy là một sai lầm. 

![](images/stat_ch11.pdf-0010-03.png)

### Bài tập Phần C 

1. Một số đường hồi quy khác nhau được sử dụng để dự báo giá của một cổ phiếu (từ các biến độc lập - independent variables khác nhau). Biểu đồ tần suất (histogram) cho các phần dư từ mỗi đường thẳng được phác thảo dưới đây. Hãy ghép các mô tả với biểu đồ tần suất tương ứng: 

   - (a) sai số r.m.s. = $5 (b) sai số r.m.s. = $15 (c) có điều gì đó không ổn 

![](images/stat_ch11.pdf-0010-07.png)

2. Một vài đường hồi quy được sử dụng để dự báo mức lương hàng tháng tại một công ty nọ, từ các biến độc lập khác nhau. Các biểu đồ phần dư từ mỗi hồi quy được hiển thị bên dưới. Hãy ghép các mô tả với biểu đồ tương ứng. Giải thích. (Bạn có thể sử dụng cùng một mô tả nhiều lần.) 

   - (a) sai số r.m.s. = $1,000 (b) sai số r.m.s. = $5,000 (c) có điều gì đó không ổn 

![](images/stat_ch11.pdf-0010-10.png)

3. Hãy nhìn vào hình bên dưới. 

   - (a) Độ lệch chuẩn (SD) của _y_ là khoảng 0.6, 1.0, hay 2.0? 

   - (b) Độ lệch chuẩn (SD) của các phần dư là khoảng 0.6, 1.0, hay 2.0? 

   - (c) Lấy các điểm trong biểu đồ phân tán có tọa độ _x_ nằm giữa 4.5 và 5.5. Độ lệch chuẩn của các tọa độ _y_ của chúng là khoảng 0.6, 1.0, hay 2.0? 

![](images/stat_ch11.pdf-0011-06.png)

_Đáp án cho các bài tập này có ở trang A64._ 

#### 4. QUAN SÁT CÁC DẢI DỌC (VERTICAL STRIPS) 

Hình 8 lặp lại biểu đồ phân tán về chiều cao của 1.078 cặp cha con trong nghiên cứu của Pearson (phần 1 của Chương 8). Các gia đình có người cha cao 64 inch (làm tròn đến inch gần nhất) được biểu diễn trong dải dọc (vertical strip) ở bên trái. Biểu đồ tần suất cho chiều cao của những người con trai trong các gia đình này được hiển thị ở phía dưới hình (đường nét liền - solid line). Các gia đình có người cha cao 72 inch được biểu diễn trong dải dọc ở bên phải. Biểu đồ tần suất cho chiều cao của những người con trai đó cũng được hiển thị (đường nét đứt - dashed line). Biểu đồ tần suất nét đứt nằm xa hơn về phía bên phải so với biểu đồ nét liền: tính trung bình, những người cha cao hơn thì có con trai cao hơn. Tuy nhiên, cả hai biểu đồ tần suất đều có hình dạng tương tự nhau, và có mức độ phân tán (spread) gần như bằng nhau.<sup>3</sup> 

Khi tất cả các dải dọc trong một biểu đồ phân tán đều thể hiện mức độ phân tán tương tự nhau, biểu đồ này được gọi là có _phương sai đồng nhất_ (homoscedastic). Biểu đồ phân tán trong Hình 8 có tính phương sai đồng nhất. Khoảng biến thiên (range) chiều cao của con trai tại một chiều cao nhất định của người cha sẽ lớn hơn ở phần giữa của bức hình, nhưng đó chỉ là vì có nhiều gia đình tập trung ở mức trung bình hơn so với hai phía cực đoan. Độ lệch chuẩn chiều cao của con trai tại một chiều cao nhất định của người cha gần như không đổi từ đầu này đến đầu kia của bức hình. _Homo_ có nghĩa là “giống nhau,” _scedastic_ có nghĩa là “phân tán.” Sự đồng nhất phương sai (_Homoscedasticity_) là một từ khủng khiếp, nhưng các nhà thống kê khăng khăng sử dụng nó: chúng ta thì thích gọi nó là “hình quả bóng bầu dục” (football-shaped) hơn.<sup>4</sup> 

Khi biểu đồ phân tán có dạng hình quả bóng bầu dục, các sai số dự báo sẽ tương tự nhau dọc theo toàn bộ đường hồi quy. Trong Hình 8, đường hồi quy để dự báo chiều cao của con trai từ chiều cao của người cha có sai số r.m.s. là 2.3 inch. Nếu người cha cao 64 inch, mức dự báo cho chiều cao của con trai là 67 inch, và con số này có khả năng sai số trong khoảng 2.3 inch. Nếu người cha cao 72 inch, mức dự báo cho chiều cao của con trai là 71 inch, và con số này cũng có khả năng sai số với cùng một lượng tương đương, khoảng 2.3 inch.<sup>5</sup> 

Hình 8. Biểu đồ phân tán có phương sai đồng nhất (Homoscedastic). Chiều cao của các cặp cha con. Các gia đình có người cha cao 64 inch được biểu diễn trong dải dọc nét liền: biểu đồ tần suất nét liền dành cho chiều cao của những người con trai đó. Các gia đình có người cha cao 72 inch được biểu diễn trong dải dọc nét đứt; biểu đồ tần suất nét đứt dành cho chiều cao của những người con trai đó. Hai biểu đồ tần suất có hình dạng tương tự nhau, và độ lệch chuẩn (SD) của chúng gần như bằng nhau.

![](images/stat_ch11.pdf-0012-03.png)

Để so sánh, Biểu đồ 9 thể hiện biểu đồ phân tán _phương sai không đồng nhất_ (heteroscedastic - _hetero_ có nghĩa là "khác nhau") của thu nhập (income) theo học vấn (education). Khi học vấn tăng lên, thu nhập trung bình tăng lên, và mức độ phân tán của thu nhập cũng vậy. Khi biểu đồ phân tán có phương sai không đồng nhất, phương pháp hồi quy sẽ sai số với các mức độ khác nhau ở các phần khác nhau của biểu đồ. Trong Biểu đồ 9, sai số toàn phương trung bình (r.m.s. error) của đường hồi quy là khoảng $19.000. Tuy nhiên, việc dự đoán thu nhập của những người có học vấn cao lại khó khăn hơn khá nhiều. Với 8 năm đi học, các sai số dự đoán vào khoảng $6.000. Ở mức 12 năm, sai số tăng lên tới khoảng $15.000 hoặc cỡ đó. Ở mức 16 năm, sai số thậm chí còn tăng cao hơn, lên tới khoảng $27.000 hoặc cỡ đó. Trong trường hợp này, sai số r.m.s. của đường hồi quy đưa ra một loại sai số trung bình—trên tất cả các giá trị $x$ khác nhau.

Biểu đồ 9. Biểu đồ phân tán có phương sai không đồng nhất (heteroscedastic). Thu nhập và học vấn (số năm đi học đã hoàn thành) đối với một mẫu gồm 570 phụ nữ California ở độ tuổi 25–29 vào năm 2005.<sup>6</sup> Đường hồi quy cũng được hiển thị.

![](images/stat_ch11.pdf-0013-04.png)

![](images/stat_ch11.pdf-0013-05.png)

![](images/stat_ch11.pdf-0013-06.png)

![](images/stat_ch11.pdf-0013-07.png)

Giả sử rằng một biểu đồ phân tán có dạng hình quả bóng bầu dục (football-shaped). Lấy các điểm trong một dải dọc hẹp. Chúng sẽ lệch khỏi đường hồi quy (lên hoặc xuống) với các mức xấp xỉ bằng kích thước của sai số r.m.s. Nếu biểu đồ có phương sai không đồng nhất, không nên sử dụng sai số r.m.s. cho các dải dọc riêng lẻ.

![](images/stat_ch11.pdf-0013-09.png)

### Bài tập phần D

1. Năm 1937, bài kiểm tra IQ Stanford-Binet đã được chuẩn hóa lại với hai dạng (L và M). Một số lượng lớn đối tượng đã thực hiện cả hai bài kiểm tra. Kết quả có thể được tóm tắt như sau:

| Bài kiểm tra | Trung bình (Average) | Độ lệch chuẩn (SD) | Hệ số tương quan ($r$) |
|---|---|---|---|
| Dạng L | $\approx 100$ | $\approx 15$ | |
| Dạng M | $\approx 100$ | $\approx 15$ | $\approx 0.80$ |

- (a) Đúng hay sai, và giải thích: đường hồi quy để dự đoán điểm số ở dạng M từ điểm số ở dạng L có sai số r.m.s. khoảng 9 điểm.

- (b) Giả sử biểu đồ phân tán trông giống như hình (i) bên dưới. Nếu ai đó đạt điểm 130 ở dạng L, phương pháp hồi quy dự đoán điểm số ở dạng M là 124. Đúng hay sai, và giải thích: dự đoán này có khả năng sai số chừng 9 điểm hoặc cỡ đó.

- (c) Lặp lại câu hỏi trên, nếu biểu đồ phân tán trông giống như hình (ii).

![](images/stat_ch11.pdf-0014-07.png)

2. Dữ liệu trong Biểu đồ 8 có thể được tóm tắt như sau:

| Đối tượng | Chiều cao trung bình | Độ lệch chuẩn (SD) | Hệ số tương quan ($r$) |
|---|---|---|---|
| Bố | $\approx 68$ inch | $\approx 2.7$ inch | |
| Con trai | $\approx 69$ inch | $\approx 2.7$ inch | $\approx 0.5$ |

   - (a) Tìm sai số r.m.s. của đường hồi quy để dự đoán chiều cao của con trai từ chiều cao của người bố.

   - (b) Nếu một người bố cao 72 inch, hãy dự đoán chiều cao của con trai ông ấy.

   - (c) Dự đoán này có khả năng sai số khoảng bao nhiêu inch. Nếu cần thêm thông tin, hãy cho biết đó là thông tin gì, và tại sao.

   - (d) Lặp lại phần (b) và (c), nếu người bố cao 66 inch.

3. Dữ liệu trong Biểu đồ 9 có thể được tóm tắt như sau:

| Biến số | Trung bình | Độ lệch chuẩn (SD) | Hệ số tương quan ($r$) |
|---|---|---|---|
| Học vấn | $\approx 13.0$ năm | $\approx 3.4$ năm | |
| Thu nhập | $\approx \$18.000$ | $\approx \$20.000$ | $\approx 0.37$ |

- (a) Tìm sai số r.m.s. của đường hồi quy để dự đoán thu nhập từ học vấn.

- (b) Dự đoán thu nhập của một người phụ nữ có 16 năm đi học.

- (c) Dự đoán này có khả năng sai số khoảng bao nhiêu đô la. Nếu cần thêm thông tin, hãy cho biết đó là thông tin gì, và tại sao.

- (d) Lặp lại phần (b) và (c), đối với một người phụ nữ có 8 năm đi học.

4. Hình dưới đây là biểu đồ phân tán về độ tuổi của các người chồng và người vợ ở Indiana. Dữ liệu từ Khảo sát Dân số Hiện tại tháng 3 năm 2005.<sup>7</sup> Dải dọc đại diện cho các gia đình mà độ tuổi nằm trong khoảng từ ___ đến ___ tuổi.

![](images/stat_ch11.pdf-0015-03.png)

5. (Tiếp tục Bài tập 4.) Điền vào chỗ trống, sử dụng các tùy chọn được cho dưới đây.

      - 0.25 | 0.5 | 0.95 | 1 | 5 | 15 | 25 | 50

   - (a) Độ tuổi trung bình của tất cả các người chồng là khoảng ____ ; độ lệch chuẩn (SD) là khoảng ____.

![](images/stat_ch11.pdf-0015-07.png)

   - (b) Độ tuổi trung bình của tất cả các người vợ là khoảng ____ ; độ lệch chuẩn (SD) là khoảng ____.

   - (c) Hệ số tương quan giữa độ tuổi của tất cả các người chồng và người vợ là khoảng ____.

   - (d) Trong số các gia đình được vẽ trên dải dọc, độ tuổi trung bình của các người vợ là khoảng ____ ; độ lệch chuẩn (SD) là khoảng ____.

   - (e) Trong số các gia đình được vẽ trên dải dọc, hệ số tương quan giữa độ tuổi của người chồng và người vợ là khoảng ____.

6. (Tiếp tục Bài tập 4 và 5.)

   - (a) SD được tính cho độ tuổi của—

      - (i) tất cả các người vợ, và

      - (ii) những người vợ có chồng từ 20–30 tuổi.

   SD nào lớn hơn? Hay các SD này xấp xỉ bằng nhau?

- (b) SD được tính cho độ tuổi của—

   - (i) tất cả các người vợ, và

   - (ii) những người vợ có chồng sinh vào tháng Ba.

   SD nào lớn hơn? Hay các SD này xấp xỉ bằng nhau?

7. Trong một nghiên cứu về các cặp sinh đôi nam cùng trứng, chiều cao trung bình được tìm thấy là khoảng 68 inch, với SD khoảng 3 inch. Hệ số tương quan giữa chiều cao của các cặp sinh đôi là khoảng 0.95, và biểu đồ phân tán có dạng hình quả bóng bầu dục (football-shaped).

   - (a) Bạn phải đoán chiều cao của một trong hai anh em sinh đôi này, mà không có thêm bất kỳ thông tin nào. Bạn sẽ sử dụng phương pháp nào?

   - (b) Tìm sai số r.m.s. cho phương pháp ở phần (a).

   - (c) Một trong hai anh em sinh đôi đang đứng trước mặt bạn. Bạn phải đoán chiều cao của người anh em sinh đôi còn lại. Bạn sẽ sử dụng phương pháp nào? (Ví dụ: giả sử người bạn nhìn thấy cao 6 foot 6 inch.)

   - (d) Tìm sai số r.m.s. cho phương pháp ở phần (c).

_Đáp án cho các bài tập này nằm trên các trang A64–65._

#### 5. SỬ DỤNG ĐƯỜNG CONG CHUẨN BÊN TRONG MỘT DẢI DỌC

Thường thì chúng ta có thể sử dụng xấp xỉ chuẩn (normal approximation) khi làm việc bên trong một dải dọc. Để điều này hợp lệ, biểu đồ phân tán phải có dạng hình quả bóng bầu dục, với các điểm nằm rải rác dày đặc ở tâm của hình và mờ dần về phía các rìa. Biểu đồ 8 là một ví dụ điển hình. Mặt khác, nếu biểu đồ phân tán có phương sai không đồng nhất (Biểu đồ 9), hoặc thể hiện một mẫu phi tuyến tính (Biểu đồ 7), thì không nên sử dụng phương pháp của phần này. Với dữ liệu về chiều cao-cân nặng trong Biểu đồ 6, đường cong chuẩn cũng sẽ không hoạt động đặc biệt tốt: đám mây điểm không có hình quả bóng bầu dục, nó bị kéo dài ở trên cùng và ép lại ở phía dưới.

_Ví dụ 1._ Một trường luật tìm thấy mối quan hệ sau đây giữa điểm LSAT và điểm số năm nhất (đối với những sinh viên hoàn thành năm đầu tiên):

| Điểm số | Trung bình | Độ lệch chuẩn (SD) | Hệ số tương quan ($r$) |
|---|---|---|---|
| Điểm LSAT | $162$ | $6$ | |
| Điểm số năm nhất | $68$ | $10$ | $0.60$ |

Biểu đồ phân tán có dạng hình quả bóng bầu dục.

- (a) Khoảng bao nhiêu phần trăm sinh viên có điểm số năm nhất trên 75?

- (b) Trong số những sinh viên đạt 165 điểm LSAT, khoảng bao nhiêu phần trăm có điểm số năm nhất trên 75?

_Lời giải. Phần (a)_. Đây là một bài toán xấp xỉ chuẩn đơn giản. Kết quả LSAT và hệ số tương quan $r$ không liên quan đến nó.

![](images/stat_ch11.pdf-0016-15.png)

_Phần (b)._ Đây là một bài toán mới. Nó nói về một nhóm sinh viên đặc biệt — những người đã đạt 165 điểm trong kỳ thi LSAT. Những sinh viên này đều nằm trong cùng một dải dọc (Biểu đồ 10). Điểm số năm nhất của họ tạo thành một tập dữ liệu mới. Để thực hiện xấp xỉ chuẩn, bạn cần giá trị trung bình và độ lệch chuẩn (SD) của tập dữ liệu mới này.

Biểu đồ 10. Một biểu đồ phân tán dạng hình quả bóng bầu dục. Lấy các điểm nằm bên trong một dải dọc hẹp. Các giá trị $y$ của chúng tạo thành một tập dữ liệu mới. Giá trị trung bình mới được đưa ra bởi phương pháp hồi quy. SD mới được đưa ra bởi sai số r.m.s. của đường hồi quy. Bên trong dải này, một giá trị $y$ điển hình sẽ nằm quanh giá trị trung bình mới—cộng trừ SD mới.

![](images/stat_ch11.pdf-0017-03.png)

_Giá trị trung bình mới._ Những sinh viên đạt 165 điểm trong kỳ thi LSAT có thành tích tốt hơn mức trung bình. Với tư cách là một nhóm, họ sẽ làm tốt hơn mức trung bình trong năm đầu tiên ở trường luật — mặc dù có một lượng phân tán đáng kể (phân tán dọc bên trong dải). Giá trị trung bình của nhóm có thể được ước lượng bằng phương pháp hồi quy: 165 cao hơn 0.5 SD so với mức trung bình, do đó nhóm sẽ đạt điểm số cao hơn mức trung bình trong năm nhất khoảng $r \times 0.5 = 0.6 \times 0.5 = 0.3$ SD. Con số này tương đương với $0.3 \times 10 = 3$ điểm. Giá trị trung bình mới là $68 + 3 = 71$.

_Độ lệch chuẩn (SD) mới._ Những sinh viên đạt 165 điểm LSAT là một nhóm nhỏ hơn và đồng nhất hơn. Vì vậy, SD của điểm số năm nhất của họ nhỏ hơn 10 điểm. Nhỏ hơn bao nhiêu? Vì biểu đồ có dạng hình quả bóng bầu dục, nên sự phân tán xung quanh đường hồi quy trong mỗi dải dọc là xấp xỉ bằng nhau, và được cho bởi sai số r.m.s. đối với đường hồi quy (phần 4). SD mới là:

![](images/stat_ch11.pdf-0017-07.png)

(Chúng ta đang dự đoán điểm số năm nhất từ điểm LSAT, vì vậy sai số được tính theo điểm số năm nhất: 10 sẽ được đưa vào công thức, chứ không phải 6.) Một sinh viên điển hình đạt khoảng 165 điểm LSAT sẽ có điểm số năm nhất khoảng 71, xê dịch trong khoảng cộng trừ 8 điểm. Giá trị trung bình mới là 71, và SD mới là 8.

_Xấp xỉ chuẩn_ là bước cuối cùng. Bước này được thực hiện như bình thường, nhưng được dựa trên giá trị trung bình mới và SD mới.

![](images/stat_ch11.pdf-0017-10.png)

Tại sao độ lệch chuẩn (SD) mới lại nhỏ hơn? Hãy nhìn vào hình 10: độ phân tán theo chiều dọc trong dải này ít hơn so với toàn bộ biểu đồ. Xem thêm các bài tập 4–6 ở trang 194. 

![](images/stat_ch11.pdf-0018-02.png)

![](images/stat_ch11.pdf-0018-03.png)

![](images/stat_ch11.pdf-0018-04.png)

Giả sử rằng một biểu đồ phân tán có dạng hình quả bóng bầu dục (football-shaped). Lấy các điểm nằm trong một dải dọc hẹp. Các giá trị _y_ của chúng tạo thành một tập dữ liệu mới. Giá trị trung bình mới được ước lượng bằng phương pháp hồi quy (regression method). Độ lệch chuẩn (SD) mới xấp xỉ bằng sai số toàn phương trung bình (r.m.s. error) của đường hồi quy. 

![](images/stat_ch11.pdf-0018-06.png)

Phép xấp xỉ phân phối chuẩn (normal approximation) có thể được thực hiện như thông thường, dựa trên giá trị trung bình mới và SD mới. 

_Lưu ý kỹ thuật._ Bạn có thể làm gì với dữ liệu phi tuyến tính (non-linear) hoặc có phương sai sai số thay đổi (heteroscedastic)? Thường thì một phép biến đổi (transformation) sẽ hữu ích — ví dụ, lấy logarit. Khung bên trái trong hình 11 hiển thị biểu đồ phân tán của độ sâu Secchi (một thước đo độ trong của nước) so với tổng nồng độ diệp lục (một thước đo lượng tảo trong nước).<sup>8</sup> Dữ liệu này phi tuyến tính và có phương sai sai số thay đổi. Khung bên phải hiển thị cùng bộ dữ liệu đó, sau khi đã lấy logarit: biểu đồ lúc này trông giống hình quả bóng bầu dục hơn. 

Hình 11. Khung bên trái: biểu đồ phân tán của độ sâu Secchi theo tổng nồng độ diệp lục. (Đơn vị của nồng độ diệp lục là ppb, hay phần tỷ trong nước.) Khung bên phải: dữ liệu đã được biến đổi bằng cách lấy logarit cơ số 10. 

![](images/stat_ch11.pdf-0018-10.png)

### Bài tập nhóm E 

1. Pearson và Lee đã thu được các kết quả sau cho khoảng 1.000 gia đình: 

      - chiều cao trung bình của chồng ≈ 68 inch, SD ≈ 2,7 inch; chiều cao trung bình của vợ ≈ 63 inch, SD ≈ 2,5 inch, _r_ ≈ 0,25 

   - (a) Tỷ lệ phần trăm phụ nữ cao hơn 5 feet 8 inch là bao nhiêu? 

   - (b) Trong số những phụ nữ kết hôn với nam giới cao 6 feet, tỷ lệ phần trăm phụ nữ cao hơn 5 feet 8 inch là bao nhiêu? 

2. Từ cùng một nghiên cứu: 

chiều cao trung bình của bố ≈ 68 inch, SD ≈ 2,7 inch; chiều cao trung bình của con trai ≈ 69 inch, SD ≈ 2,7 inch, _r_ ≈ 0,50 

   - (a) Tỷ lệ phần trăm con trai cao hơn 6 feet là bao nhiêu? 

   - (b) Tỷ lệ phần trăm các ông bố cao 6 feet có con trai cao hơn 6 feet là bao nhiêu? 

3. Từ cùng một nghiên cứu: 

chiều cao trung bình của nam giới ≈ 68 inch, SD ≈ 2,7 inch; chiều dài cẳng tay trung bình ≈ 18 inch, SD ≈ 1 inch, _r_ ≈ 0,80 

- (a) Tỷ lệ phần trăm nam giới có cẳng tay dài 18 inch (làm tròn đến inch gần nhất) là bao nhiêu? 

- (b) Trong số những nam giới cao 68 inch, tỷ lệ phần trăm người có cẳng tay dài 18 inch (làm tròn đến inch gần nhất) là bao nhiêu? 

_Đáp án cho các bài tập này nằm ở trang A65._ 

#### 6. BÀI TẬP ÔN TẬP 

_Các bài tập ôn tập có thể bao gồm kiến thức từ các chương trước._ 

1. Sai số toàn phương trung bình (r.m.s. error) của đường hồi quy để dự đoán _y_ từ _x_ là 

![](images/stat_ch11.pdf-0019-14.png)

. 

(i) SD của _y_ (iv) _r_ × SD của _x_ (ii) SD của _x_ (v) $\sqrt{1 - r^2}$ × SD của _y_ (iii) _r_ × SD của _y_ (vi) $\sqrt{1 - r^2}$ × SD của _x_ 

2. Một chương trình máy tính được phát triển để dự đoán điểm trung bình (GPA) của sinh viên năm nhất đại học từ điểm GPA thời trung học của họ. Chương trình này được thử nghiệm trên một lớp học đã biết trước điểm GPA đại học. Sai số toàn phương trung bình (r.m.s. error) là 3,12. Có điều gì sai sót ở đây không? Trả lời có hoặc không, và giải thích. 

3. Tuddenham và Snyder đã thu được các kết quả sau cho 66 bé trai ở California tại các độ tuổi 6 và 18 (biểu đồ phân tán có dạng hình quả bóng bầu dục):<sup>9</sup> 

chiều cao trung bình lúc 6 tuổi ≈ 3 feet 10 inch, SD ≈ 1,7 inch; chiều cao trung bình lúc 18 tuổi ≈ 5 feet 10 inch, SD ≈ 2,5 inch, _r_ ≈ 0,80 

   - (a) Tìm sai số toàn phương trung bình (r.m.s. error) cho dự đoán hồi quy của chiều cao lúc 18 tuổi từ chiều cao lúc 6 tuổi. 

   - (b) Tìm sai số toàn phương trung bình (r.m.s. error) cho dự đoán hồi quy của chiều cao lúc 6 tuổi từ chiều cao lúc 18 tuổi. 

4. Một phân tích thống kê đã được thực hiện đối với điểm thi giữa kỳ và cuối kỳ trong một khóa học lớn, với các kết quả sau: 

điểm trung bình giữa kỳ ≈ 50, SD ≈ 25; điểm trung bình cuối kỳ ≈ 55, SD ≈ 15, _r_ ≈ 0,60 

Biểu đồ phân tán có dạng hình quả bóng bầu dục. Đối với mỗi sinh viên, điểm cuối kỳ được dự đoán từ điểm giữa kỳ bằng cách sử dụng đường hồi quy. 

- (a) Đối với khoảng 1/3 số sinh viên, dự đoán điểm cuối kỳ bị sai lệch (off) hơn ... điểm. Các lựa chọn: 6, 9, 12, 15, 25. 

- (b) 

- (c) Dự đoán này có khả năng bị sai lệch khoảng ... điểm. Các lựa chọn: 6, 9, 12, 15, 25. 

Giải thích các câu trả lời của bạn. 

5. Sử dụng dữ liệu trong bài tập 4 để trả lời các câu hỏi sau. 

   - (a) Khoảng bao nhiêu phần trăm sinh viên đạt trên 80 điểm ở bài thi cuối kỳ? 

   - (b) Trong số những sinh viên đạt 80 điểm giữa kỳ, khoảng bao nhiêu phần trăm đạt trên 80 điểm ở bài thi cuối kỳ? 

Giải thích các câu trả lời của bạn. 

6. Trong một nghiên cứu về học sinh trung học, người ta đã tìm thấy một tương quan thuận (positive correlation) giữa số giờ làm bài tập về nhà mỗi tuần và điểm số trên các bài kiểm tra thành tích chuẩn hóa (standardized achievement tests). Các nhà điều tra kết luận rằng việc làm bài tập về nhà giúp chuẩn bị cho học sinh trước các bài kiểm tra này. Kết luận đó có được suy ra từ dữ liệu không? Trả lời có hoặc không, và giải thích ngắn gọn. 

7. Sinh viên năm nhất tại một trường đại học lớn phải tham gia một loạt bài kiểm tra năng lực. Những sinh viên đạt điểm cao trong bài kiểm tra toán cũng có xu hướng đạt điểm cao trong bài kiểm tra vật lý. Ở cả hai bài kiểm tra, điểm trung bình đều là 60; các SD cũng giống nhau. Biểu đồ phân tán có dạng hình quả bóng bầu dục. Trong số những sinh viên đạt khoảng 75 điểm trong bài kiểm tra toán: 

   - (i) chỉ khoảng một nửa đạt trên 75 điểm trong bài kiểm tra vật lý. (ii) hơn một nửa đạt trên 75 điểm trong bài kiểm tra vật lý. 

   - (iii) chưa tới một nửa đạt trên 75 điểm trong bài kiểm tra vật lý. 

Chọn một lựa chọn và giải thích. 

8. Hội chứng giảm áp (the bends) gây ra do sự thay đổi nhanh chóng của áp suất không khí, dẫn đến sự hình thành các bọt khí nitơ trong máu. Triệu chứng là các cơn đau cấp tính, đôi khi dẫn đến liệt và tử vong. Trong Thế chiến II, các phi công mắc hội chứng này trong những chiến dịch diễn tập nhất định. Người ta có thể mô phỏng các điều kiện này trong một buồng áp suất. Do đó, các học viên phi công đã được kiểm tra dưới các điều kiện này một lần, vào đầu khóa huấn luyện. Nếu họ mắc hội chứng giảm áp (chỉ các trường hợp nhẹ được gây ra), họ sẽ bị loại khỏi khóa đào tạo với lý do họ có khả năng cao sẽ mắc hội chứng này dưới các điều kiện chiến đấu thực tế. Quy trình này đã bị nhà thống kê Joe Berkson chỉ trích gay gắt, và ông đã thuyết phục Không quân nhân bản (replicate) thử nghiệm — tức là, lặp lại thử nghiệm đó vài lần cho mỗi học viên. 

   - (a) Tại sao Berkson lại đề xuất điều này? 

   - (b) Đưa ra một ví dụ khác mà việc nhân bản (lặp lại thử nghiệm) là hữu ích. 

9. Hàng năm, các giải đấu bóng chày lớn vinh danh những cầu thủ năm nhất xuất sắc nhất với danh hiệu “Tân binh của năm” (Rookie of the Year). Tỷ lệ đánh bóng thành công (batting average) trung bình tổng thể của các Tân binh của năm là khoảng 0,290, cao hơn nhiều so với tỷ lệ đánh bóng thành công của toàn giải là 0,260. Tuy nhiên, các Tân binh của năm lại không thi đấu tốt như vậy trong năm thứ hai của họ — tỷ lệ đánh bóng thành công tổng thể trong mùa giải thứ hai của họ chỉ là 0,275. Các ký giả bóng chày gọi đây là “hiện tượng sa sút năm thứ hai” (sophomore slump), với ý tưởng rằng các cầu thủ ngôi sao bị phân tâm bởi các hoạt động bên ngoài như đại diện sản phẩm và xuất hiện trên truyền hình. Dữ liệu này có ủng hộ ý tưởng về sự sa sút năm thứ hai không? Trả lời có hoặc không, và giải thích ngắn gọn.<sup>10</sup> 

10. Một nghiên cứu đã được thực hiện về mối quan hệ giữa giá cổ phiếu vào ngày giao dịch cuối cùng của năm 2005 và ngày giao dịch cuối cùng của năm 2006. Một công thức đã được phát triển để dự đoán giá cổ phiếu năm 2006 từ giá năm 2005, sử dụng dữ liệu của 100 cổ phiếu. Hiện tại, một nhà phân tích đang xem xét các kết quả này. Dữ liệu của 5 trong số 100 cổ phiếu được hiển thị dưới đây; giá tính bằng đô la. Phương pháp hồi quy có được sử dụng để dự đoán giá năm 2006 từ giá năm 2005 hay không? Trả lời có hoặc không và giải thích. Nếu bạn cần thêm thông tin, hãy giải thích lý do tại sao. 

| _Cổ phiếu (Stock)_ | _Giá năm 2005 (thực tế)_ | _Giá năm 2006 (dự đoán)_ | _Giá năm 2006 (thực tế)_ |
|---|---|---|---|
| A | 10 | 8 | 8 |
| B | 10 | 8 | 3 |
| C | 12 | 13 | 17 |
| D | 14 | 12 | 6 |
| E | 15 | 20 | 27 |

![](images/stat_ch11.pdf-0021-04.png)

11. Hình dưới đây là một biểu đồ phân tán của thu nhập theo học vấn, đối với một mẫu đại diện (representative sample) nam giới trong độ tuổi 25–29 ở Texas. Hay là có điều gì sai sót? Giải thích ngắn gọn. (“Trình độ học vấn” nghĩa là số năm đi học đã hoàn thành, không tính mẫu giáo.) 

![](images/stat_ch11.pdf-0021-06.png)

12. Đối với nam giới trong độ tuổi 25–34 thuộc nhóm HANES5, mối quan hệ giữa học vấn (số năm đi học đã hoàn thành) và huyết áp tâm thu (systolic blood pressure) có thể được tóm tắt như sau.<sup>11</sup> 

số năm đi học trung bình ≈ 13 năm, SD ≈ 3 năm; huyết áp trung bình ≈ 119 mm, SD ≈ 11 mm, _r_ ≈ −0,1 

Một người đàn ông trong mẫu có số năm đi học là 20 năm, và huyết áp của anh ta là 118 mm. Đúng hay sai, và giải thích: so với những người đàn ông khác cùng trình độ học vấn với anh ta, huyết áp của anh ta hơi cao. 

#### 7. TÓM TẮT 

1. Khi đường hồi quy được sử dụng để dự đoán _y_ từ _x_ , chênh lệch giữa giá trị thực tế và giá trị dự đoán được gọi là một _phần dư_ (residual), hay sai số dự đoán (prediction error). 

2. Trong một biểu đồ phân tán, khoảng cách theo chiều dọc của một điểm nằm trên hoặc dưới đường hồi quy là phiên bản đồ họa tương đương của sai số dự đoán được tạo ra bởi phương pháp hồi quy. 

3. _Sai số toàn phương trung bình_ (r.m.s. error) của đường hồi quy là căn bậc hai trung bình bình phương (root-mean-square) của các phần dư. Nó đo lường độ chính xác của các dự đoán hồi quy. Các dự đoán bị sai lệch một lượng có độ lớn tương đương với sai số r.m.s. Đối với nhiều biểu đồ phân tán, khoảng 68% các dự đoán sẽ chính xác trong phạm vi một sai số r.m.s. Khoảng 95% sẽ chính xác trong phạm vi hai sai số r.m.s. 

4. SD của _y_ bằng với sai số r.m.s. của một đường ngang đi qua giá trị trung bình của _y_ . Sai số r.m.s. của đường hồi quy nhỏ hơn một hệ số nhân là $\sqrt{1 - r^2}$ . Do đó, sai số r.m.s. cho đường hồi quy của _y_ theo _x_ có thể được tính theo công thức: 

![](images/stat_ch11.pdf-0022-09.png)

5. Sau khi thực hiện một phép hồi quy, các nhà thống kê thường vẽ đồ thị các phần dư. Nếu _biểu đồ phần dư_ (residual plot) cho thấy một mẫu hình (pattern) nào đó, phép hồi quy có thể đã không phù hợp. 

6. Khi tất cả các dải dọc trong một biểu đồ phân tán đều cho thấy mức độ phân tán tương tự nhau, biểu đồ đó có tính _phương sai sai số không đổi_ (homoscedastic): các sai số dự đoán có độ lớn tương tự nhau dọc theo toàn bộ đường hồi quy. Khi biểu đồ phân tán có _phương sai sai số thay đổi_ (heteroscedastic), các sai số dự đoán sẽ khác nhau ở các phần khác nhau của biểu đồ. Các biểu đồ có dạng hình quả bóng bầu dục là homoscedastic. 

7. Giả sử rằng một biểu đồ phân tán có dạng hình quả bóng bầu dục. Lấy các điểm nằm bên trong một dải dọc hẹp. Các giá trị _y_ của chúng tạo thành một tập dữ liệu mới. Giá trị trung bình mới được ước lượng bằng phương pháp hồi quy. SD mới xấp xỉ bằng sai số r.m.s. của đường hồi quy. Và phép xấp xỉ phân phối chuẩn có thể được thực hiện như thông thường, dựa trên giá trị trung bình mới và SD mới.

