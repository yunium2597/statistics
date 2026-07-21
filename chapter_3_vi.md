3 

# Hồi quy tuyến tính 

Chương này nói về _hồi quy tuyến tính (linear regression)_, một phương pháp tiếp cận rất đơn giản cho học có giám sát (supervised learning). Cụ thể, hồi quy tuyến tính là một công cụ hữu ích để dự đoán một biến phản hồi định lượng. Nó đã xuất hiện từ lâu và là chủ đề của vô số sách giáo khoa. Mặc dù nó có vẻ hơi nhàm chán so với một số phương pháp học thống kê hiện đại hơn được mô tả ở các chương sau của cuốn sách này, hồi quy tuyến tính vẫn là một phương pháp học thống kê hữu ích và được sử dụng rộng rãi. Hơn nữa, nó đóng vai trò là điểm khởi đầu tốt cho các phương pháp tiếp cận mới hơn: như chúng ta sẽ thấy ở các chương sau, nhiều phương pháp học thống kê phức tạp có thể được xem là sự tổng quát hóa hoặc mở rộng của hồi quy tuyến tính. Do đó, tầm quan trọng của việc có một sự hiểu biết tốt về hồi quy tuyến tính trước khi nghiên cứu các phương pháp học phức tạp hơn là không thể nói quá. Trong chương này, chúng tôi xem xét một số ý tưởng chính làm cơ sở cho mô hình hồi quy tuyến tính, cũng như phương pháp bình phương tối thiểu (least squares) được sử dụng phổ biến nhất để khớp mô hình này.

Hãy nhớ lại dữ liệu `Advertising` từ Chương 2. Hình 2.1 hiển thị `sales` (bằng hàng nghìn đơn vị) cho một sản phẩm cụ thể như một hàm của ngân sách quảng cáo (bằng hàng nghìn đô la) cho các phương tiện `TV`, `radio` và `newspaper`. Giả sử rằng trong vai trò là các nhà tư vấn thống kê, chúng tôi được yêu cầu đề xuất, trên cơ sở dữ liệu này, một kế hoạch tiếp thị cho năm tới sẽ mang lại doanh số bán sản phẩm cao. Thông tin nào sẽ hữu ích để đưa ra khuyến nghị như vậy? Dưới đây là một số câu hỏi quan trọng mà chúng ta có thể tìm cách giải quyết:

##### 60 3. Hồi quy tuyến tính 

1. _Có mối quan hệ giữa ngân sách quảng cáo và doanh số bán hàng không?_ Mục tiêu đầu tiên của chúng ta nên là xác định xem dữ liệu có cung cấp bằng chứng về mối liên hệ giữa chi phí quảng cáo và doanh số bán hàng hay không. Nếu bằng chứng là yếu, thì người ta có thể lập luận rằng không nên chi tiền cho quảng cáo! 

2. _Mối quan hệ giữa ngân sách quảng cáo và doanh số bán hàng mạnh đến mức nào?_ Giả sử rằng có một mối quan hệ giữa quảng cáo và doanh số bán hàng, chúng ta muốn biết độ mạnh của mối quan hệ này. Kiến thức về ngân sách quảng cáo có cung cấp nhiều thông tin về doanh số bán sản phẩm không? 

3. _Phương tiện truyền thông nào có liên quan đến doanh số bán hàng?_ Có phải cả ba phương tiện—TV, đài phát thanh và báo chí—đều có liên quan đến doanh số bán hàng, hay chỉ có một hoặc hai phương tiện có liên quan? Để trả lời câu hỏi này, chúng ta phải tìm cách tách rời phần đóng góp riêng lẻ của mỗi phương tiện đối với doanh số bán hàng khi chúng ta đã chi tiền cho cả ba phương tiện. 

4. _Mối liên hệ giữa mỗi phương tiện và doanh số bán hàng lớn đến mức nào?_ Cứ mỗi đô la chi cho quảng cáo trên một phương tiện truyền thông cụ thể, doanh số sẽ tăng bao nhiêu? Chúng ta có thể dự đoán chính xác đến mức nào mức tăng này? 

5. _Chúng ta có thể dự đoán doanh số trong tương lai chính xác đến mức nào?_ Đối với bất kỳ mức độ quảng cáo trên truyền hình, đài phát thanh hoặc báo chí nào, dự đoán của chúng ta về doanh số là gì và độ chính xác của dự đoán này là bao nhiêu? 

6. _Mối quan hệ có tuyến tính không?_ 

   - Nếu có một mối quan hệ xấp xỉ đường thẳng giữa chi phí quảng cáo trên các phương tiện khác nhau và doanh số bán hàng, thì hồi quy tuyến tính là một công cụ thích hợp. Nếu không, thì vẫn có thể biến đổi biến dự báo hoặc biến phản hồi để có thể sử dụng hồi quy tuyến tính. 

7. _Có sự hiệp đồng giữa các phương tiện quảng cáo không?_ Có lẽ việc chi 50.000 đô la cho quảng cáo truyền hình và 50.000 đô la cho quảng cáo trên đài phát thanh có liên quan đến doanh số bán hàng cao hơn so với việc phân bổ 100.000 đô la cho truyền hình hoặc đài phát thanh một cách riêng lẻ. Trong tiếp thị, điều này được gọi là hiệu ứng _hiệp đồng (synergy)_, trong khi ở thống kê nó được gọi là hiệu ứng _tương tác (interaction)_. hiệp đồng 

Hóa ra hồi quy tuyến tính có thể được sử dụng để trả lời từng câu hỏi này. Trước tiên, chúng ta sẽ thảo luận tất cả các câu hỏi này trong một bối cảnh chung, và sau đó quay lại chúng trong bối cảnh cụ thể này ở Mục 3.4. 

tương tác 

3.1 Hồi quy tuyến tính đơn 61 

## 3.1 Hồi quy tuyến tính đơn 

_Hồi quy tuyến tính đơn (Simple linear regression)_ đúng như tên gọi của nó: nó là một phương pháp tiếp cận rất đơn giản hồi quy tuyến tính đơn để dự đoán một biến phản hồi định lượng $Y$ trên cơ sở một biến dự báo duy nhất $X$. Nó giả định rằng có một mối quan hệ xấp xỉ tuyến tính giữa $X$ và $Y$. Về mặt toán học, chúng ta có thể viết mối quan hệ tuyến tính này như sau 

$$Y \approx \beta_0 + \beta_1 X$$

Bạn có thể đọc " $\approx$ " là _"được mô hình hóa xấp xỉ dưới dạng"_. Đôi khi chúng ta sẽ mô tả (3.1) bằng cách nói rằng chúng ta đang _hồi quy $Y$ theo $X$_ (hoặc _hồi quy $Y$ lên $X$_). Ví dụ, $X$ có thể đại diện cho quảng cáo `TV` và $Y$ có thể đại diện cho `sales`. Sau đó, chúng ta có thể hồi quy `sales` theo `TV` bằng cách khớp mô hình 

$$\text{sales} \approx \beta_0 + \beta_1 \times \text{TV}$$

Trong Phương trình 3.1, $\beta_0$ và $\beta_1$ là hai hằng số chưa biết đại diện cho các số hạng _hệ số chặn (intercept)_ và _độ dốc (slope)_ trong mô hình tuyến tính. Cùng với nhau, $\beta_0$ và $\beta_1$ được hệ số chặn biết đến như là các _hệ số (coefficients)_ hoặc _tham số (parameters)_ của mô hình. Khi chúng ta đã sử dụng dữ liệu huấn luyện của mình để tạo ra các ước lượng $\hat{\beta}_0$ và $\hat{\beta}_1$ cho các hệ số của mô hình, chúng ta hệ số độ dốc có thể dự đoán doanh số trong tương lai dựa trên một giá trị cụ thể của quảng cáo TV tham số bằng cách tính toán 

hệ số độ dốc tham số 

$$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$$

trong đó $\hat{y}$ biểu thị một dự đoán của $Y$ trên cơ sở $X = x$. Ở đây chúng ta sử dụng một ký hiệu _mũ (hat)_, $\hat{}$ , để biểu thị giá trị ước lượng cho một tham số hoặc hệ số chưa biết, hoặc để biểu thị giá trị dự đoán của biến phản hồi. 

### _3.1.1 Ước lượng các hệ số_ 

Trong thực tế, $\beta_0$ và $\beta_1$ là chưa biết. Vì vậy, trước khi chúng ta có thể sử dụng (3.1) để đưa ra dự đoán, chúng ta phải sử dụng dữ liệu để ước lượng các hệ số. Gọi 

$$(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$$

đại diện cho $n$ cặp quan sát, mỗi cặp bao gồm một phép đo của $X$ và một phép đo của $Y$. Trong ví dụ `Advertising`, tập dữ liệu này bao gồm ngân sách quảng cáo TV và doanh số bán sản phẩm ở $n = 200$ thị trường khác nhau. (Nhớ lại rằng dữ liệu được hiển thị trong Hình 2.1.) Mục tiêu của chúng ta là thu được các ước lượng hệ số $\hat{\beta}_0$ và $\hat{\beta}_1$ sao cho mô hình tuyến tính (3.1) khớp với dữ liệu có sẵn một cách tốt nhất—tức là, sao cho $y_i \approx \hat{\beta}_0 + \hat{\beta}_1 x_i$ cho $i = 1, \dots, n$. Nói cách khác, chúng ta muốn tìm một hệ số chặn $\hat{\beta}_0$ và một độ dốc $\hat{\beta}_1$ sao cho đường thẳng thu được càng gần càng tốt với $n = 200$ điểm dữ liệu. Có một số cách để đo lường sự _gần gũi (closeness)_. Tuy nhiên, phương pháp phổ biến nhất cho đến nay liên quan đến việc giảm thiểu tiêu chí _bình phương tối thiểu (least squares)_, và chúng ta thực hiện phương pháp đó trong chương này. Các phương pháp thay thế sẽ được xem xét trong bình phương tối thiểu Chương 6. 

![](images/chapter_3.pdf-0004-00.png)

**HÌNH 3.1.** _Đối với dữ liệu_ `Advertising` _, đường khớp bình phương tối thiểu cho hồi quy của_ `sales` _theo_ `TV` _được hiển thị. Đường khớp được tìm thấy bằng cách giảm thiểu tổng bình phương phần dư. Mỗi đoạn thẳng màu xám biểu diễn một phần dư. Trong trường hợp này, một đường khớp tuyến tính nắm bắt được bản chất của mối quan hệ, mặc dù nó đánh giá quá cao xu hướng ở bên trái của biểu đồ._ 

Cho $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ là dự đoán cho $Y$ dựa trên giá trị thứ $i$ của $X$. Khi đó $e_i = y_i - \hat{y}_i$ đại diện cho _phần dư (residual)_ thứ $i$—đây là sự khác biệt giữa phần dư giá trị phản hồi quan sát được thứ $i$ và giá trị phản hồi thứ $i$ được dự đoán bởi mô hình tuyến tính của chúng ta. Chúng ta định nghĩa _tổng bình phương phần dư_ (RSS) là 

tổng bình phương phần dư 

$$\text{RSS} = e_1^2 + e_2^2 + \dots + e_n^2,$$

hoặc tương đương như sau 

$$\text{RSS} = (y_1 - \hat{\beta}_0 - \hat{\beta}_1 x_1)^2 + (y_2 - \hat{\beta}_0 - \hat{\beta}_1 x_2)^2 + \dots + (y_n - \hat{\beta}_0 - \hat{\beta}_1 x_n)^2.$$

Phương pháp bình phương tối thiểu chọn $\hat{\beta}_0$ và $\hat{\beta}_1$ để giảm thiểu RSS. Sử dụng một số phép tính vi tích phân, ta có thể chỉ ra rằng các giá trị cực tiểu hóa là 

$$\hat{\beta}_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x},$$

trong đó $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^n y_i$ và $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^n x_i$ là các trung bình mẫu. Nói cách khác, (3.4) định nghĩa các _ước lượng hệ số bình phương tối thiểu_ cho hồi quy tuyến tính đơn. 

Hình 3.1 hiển thị đường khớp hồi quy tuyến tính đơn đối với dữ liệu `Advertising`, trong đó $\hat{\beta}_0 = 7.03$ và $\hat{\beta}_1 = 0.0475$. Nói cách khác, theo 

3.1 Hồi quy tuyến tính đơn 63 

![](images/chapter_3.pdf-0005-01.png)

**HÌNH 3.2.** _Biểu đồ đường đồng mức và biểu đồ ba chiều của RSS trên dữ liệu_ `Advertising` _, sử dụng_ `sales` _làm biến phản hồi và_ `TV` _làm biến dự báo. Các dấu chấm màu đỏ tương ứng với các ước lượng bình phương tối thiểu $\hat{\beta}_0$ và $\hat{\beta}_1$, được đưa ra bởi (3.4)._ 

xấp xỉ này, việc chi thêm 1.000 đô la cho quảng cáo trên TV có liên quan đến việc bán thêm khoảng 47,5 đơn vị sản phẩm. Trong Hình 3.2, chúng tôi đã tính toán RSS cho một số giá trị của $\beta_0$ và $\beta_1$, sử dụng dữ liệu quảng cáo với `sales` là biến phản hồi và `TV` là biến dự báo. Trong mỗi biểu đồ, dấu chấm màu đỏ đại diện cho cặp ước lượng bình phương tối thiểu $(\hat{\beta}_0, \hat{\beta}_1)$ được đưa ra bởi (3.4). Những giá trị này rõ ràng làm giảm thiểu RSS. 

### _3.1.2 Đánh giá độ chính xác của các ước lượng hệ số_ 

Nhớ lại từ (2.1) rằng chúng ta giả định rằng mối quan hệ _thực sự_ giữa $X$ và $Y$ có dạng $Y = f(X) + \epsilon$ đối với một hàm $f$ chưa biết nào đó, trong đó $\epsilon$ là một số hạng sai số ngẫu nhiên có trung bình bằng không. Nếu $f$ được xấp xỉ bằng một hàm tuyến tính, thì chúng ta có thể viết mối quan hệ này như sau 

$$Y = \beta_0 + \beta_1 X + \epsilon.$$

Ở đây $\beta_0$ là số hạng hệ số chặn—nghĩa là, giá trị kỳ vọng của $Y$ khi $X = 0$, và $\beta_1$ là độ dốc—mức tăng trung bình của $Y$ liên quan đến việc tăng một đơn vị của $X$. Số hạng sai số bao gồm mọi thứ mà chúng ta bỏ lỡ với mô hình đơn giản này: mối quan hệ thực sự có thể không tuyến tính, có thể có các biến khác gây ra sự thay đổi trong $Y$, và có thể có sai số đo lường. Chúng ta thường giả định rằng số hạng sai số độc lập với $X$. 

Mô hình được cho bởi (3.5) định nghĩa _đường hồi quy tổng thể (population regression line)_, đây tổng thể là xấp xỉ tuyến tính tốt nhất đối với mối quan hệ thực sự giữa $X$ và 

đường hồi quy 

64 3. Hồi quy tuyến tính 

![](images/chapter_3.pdf-0006-01.png)

**HÌNH 3.3.** _Một tập dữ liệu mô phỏng._ Trái: _Đường màu đỏ biểu diễn mối quan hệ thực sự, $f(X) = 2 + 3X$, được biết đến là đường hồi quy tổng thể. Đường màu xanh là đường bình phương tối thiểu; nó là ước lượng bình phương tối thiểu cho $f(X)$ dựa trên dữ liệu quan sát được, hiển thị bằng màu đen._ Phải: _Đường hồi quy tổng thể một lần nữa được hiển thị màu đỏ, và đường bình phương tối thiểu màu xanh đậm. Màu xanh nhạt hiển thị mười đường bình phương tối thiểu, mỗi đường được tính toán trên cơ sở một tập hợp các quan sát ngẫu nhiên riêng biệt. Mỗi đường bình phương tối thiểu là khác nhau, nhưng trung bình, các đường bình phương tối thiểu khá gần với đường hồi quy tổng thể._ 

$Y$.<sup>1</sup> Các ước lượng hệ số hồi quy bình phương tối thiểu (3.4) đặc trưng cho _đường bình phương tối thiểu_ (3.2). Bảng điều khiển bên trái của Hình 3.3 hiển thị hai bình phương tối thiểu đường này trong một ví dụ mô phỏng đơn giản. Chúng tôi đã tạo ra 100 giá trị $X$ ngẫu nhiên, và đường tạo ra 100 giá trị $Y$ tương ứng từ mô hình 

$$Y = 2 + 3X + \epsilon$$

trong đó $\epsilon$ được tạo ra từ một phân phối chuẩn với trung bình bằng không. Đường màu đỏ trong bảng điều khiển bên trái của Hình 3.3 hiển thị mối quan hệ _thực sự_, $f(X) = 2 + 3X$, trong khi đường màu xanh là ước lượng bình phương tối thiểu dựa trên dữ liệu quan sát được. Mối quan hệ thực sự nói chung là không được biết đối với dữ liệu thực tế, nhưng đường bình phương tối thiểu luôn có thể được tính toán bằng cách sử dụng các ước lượng hệ số được đưa ra trong (3.4). Nói cách khác, trong các ứng dụng thực tế, chúng ta có quyền truy cập vào một tập hợp các quan sát mà từ đó chúng ta có thể tính toán đường bình phương tối thiểu; tuy nhiên, đường hồi quy tổng thể là không quan sát được. Trong bảng điều khiển bên phải của Hình 3.3, chúng tôi đã tạo ra mười tập dữ liệu khác nhau từ mô hình được cho bởi (3.6) và vẽ mười đường bình phương tối thiểu tương ứng. Lưu ý rằng các tập dữ liệu khác nhau được tạo từ cùng một mô hình thực dẫn đến các đường bình phương tối thiểu hơi khác nhau, nhưng đường hồi quy tổng thể không quan sát được thì không thay đổi. 

> 1Giả định về tính tuyến tính thường là một mô hình làm việc hữu ích. Tuy nhiên, bất chấp những gì nhiều sách giáo khoa có thể cho chúng ta biết, chúng ta hiếm khi tin rằng mối quan hệ thực sự là tuyến tính. 

3.1 Hồi quy tuyến tính đơn 65 

Thoạt nhìn, sự khác biệt giữa đường hồi quy tổng thể và đường bình phương tối thiểu có vẻ tinh tế và khó hiểu. Chúng ta chỉ có một tập dữ liệu, vậy điều đó có nghĩa là gì khi hai đường khác nhau mô tả mối quan hệ giữa biến dự báo và biến phản hồi? Về cơ bản, khái niệm về hai đường này là một phần mở rộng tự nhiên của phương pháp thống kê tiêu chuẩn là sử dụng thông tin từ một mẫu để ước lượng các đặc điểm của một quần thể lớn. Ví dụ, giả sử rằng chúng ta quan tâm đến việc biết trung bình tổng thể $\mu$ của một biến ngẫu nhiên $Y$ nào đó. Thật không may, $\mu$ là chưa biết, nhưng chúng ta có quyền truy cập vào $n$ quan sát từ $Y$, $y_1, \dots, y_n$, mà chúng ta có thể sử dụng để ước lượng $\mu$. Một ước lượng hợp lý là $\hat{\mu} = \bar{y}$, trong đó $\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i$ là trung bình mẫu. Trung bình mẫu và trung bình tổng thể là khác nhau, nhưng nhìn chung trung bình mẫu sẽ cung cấp một ước lượng tốt về trung bình tổng thể. Theo cách tương tự, các hệ số chưa biết $\beta_0$ và $\beta_1$ trong hồi quy tuyến tính định nghĩa đường hồi quy tổng thể. Chúng ta tìm cách ước lượng các hệ số chưa biết này bằng cách sử dụng $\hat{\beta}_0$ và $\hat{\beta}_1$ được đưa ra trong (3.4). Các ước lượng hệ số này định nghĩa đường bình phương tối thiểu. 

Sự tương tự giữa hồi quy tuyến tính và ước lượng trung bình của một biến ngẫu nhiên là một sự tương tự thích hợp dựa trên khái niệm _độ chệch (bias)_. Nếu chúngúng ta sử dụng trung bình mẫu $\hat{\mu}$ để ước lượng $\mu$, ước lượng này là _không chệch (unbiased)_, theo nghĩa là độ chệch trung bình, chúng ta kỳ vọng $\hat{\mu}$ bằng $\mu$. Điều này chính xác có nghĩa là gì? Nó có nghĩa là không chệch dựa trên một tập hợp các quan sát cụ thể $y_1, \dots, y_n$, $\hat{\mu}$ có thể đánh giá quá cao $\mu$, và dựa trên một tập hợp các quan sát khác, $\hat{\mu}$ có thể đánh giá quá thấp $\mu$. Nhưng nếu chúng ta có thể lấy trung bình của một số lượng lớn các ước lượng của $\mu$ thu được từ một số lượng lớn các tập hợp quan sát, thì giá trị trung bình này sẽ _chính xác_ bằng $\mu$. Do đó, một bộ ước lượng không chệch không _có tính hệ thống_ đánh giá quá cao hoặc quá thấp tham số thực. Tính chất không chệch cũng đúng đối với các ước lượng hệ số bình phương tối thiểu được cho bởi (3.4): nếu chúng ta ước lượng $\beta_0$ và $\beta_1$ dựa trên một tập dữ liệu cụ thể, thì các ước lượng của chúng ta sẽ không chính xác bằng $\beta_0$ và $\beta_1$. Nhưng nếu chúng ta có thể lấy trung bình các ước lượng thu được qua một số lượng lớn các tập dữ liệu, thì giá trị trung bình của các ước lượng này sẽ cực kỳ chuẩn xác! Trên thực tế, chúng ta có thể thấy từ bảng điều khiển bên phải của Hình 3.3 rằng trung bình của nhiều đường bình phương tối thiểu, mỗi đường được ước lượng từ một tập dữ liệu riêng biệt, khá gần với đường hồi quy tổng thể thực sự. 

Chúng ta tiếp tục sự tương tự với việc ước lượng trung bình tổng thể $\mu$ của một biến ngẫu nhiên $Y$. Một câu hỏi tự nhiên như sau: trung bình mẫu $\hat{\mu}$ chính xác đến mức nào với tư cách là một ước lượng của $\mu$? Chúng ta đã thiết lập rằng trung bình của các $\hat{\mu}$ trên nhiều tập dữ liệu sẽ rất gần với $\mu$, nhưng một ước lượng đơn lẻ $\hat{\mu}$ có thể là một sự đánh giá quá thấp hoặc quá cao đáng kể đối với $\mu$. Ước lượng đơn lẻ của $\hat{\mu}$ đó sẽ sai lệch bao xa? Nói chung, chúng ta trả lời câu hỏi này bằng cách tính toán _sai số chuẩn (standard error)_ của $\hat{\mu}$, được viết là $\text{SE}(\hat{\mu})$. Chúng ta có chuẩn công thức nổi tiếng 

sai số 

$$\text{Var}(\hat{\mu}) = \text{SE}(\hat{\mu})^2 = \frac{\sigma^2}{n},$$

66 3. Hồi quy tuyến tính 

trong đó $\sigma$ là độ lệch chuẩn của từng giá trị thực hiện $y_i$ của $Y$.<sup>2</sup> Nói một cách sơ lược, sai số chuẩn cho chúng ta biết lượng trung bình mà ước lượng này $\hat{\mu}$ khác với giá trị thực của $\mu$. Phương trình 3.7 cũng cho chúng ta biết độ lệch này co lại như thế nào theo $n$—càng có nhiều quan sát, sai số chuẩn của $\hat{\mu}$ càng nhỏ. Theo cách tương tự, chúng ta có thể tự hỏi $\hat{\beta}_0$ và $\hat{\beta}_1$ gần với các giá trị thực $\beta_0$ và $\beta_1$ đến mức nào. Để tính toán các sai số chuẩn liên quan đến $\hat{\beta}_0$ và $\hat{\beta}_1$, chúng ta sử dụng các công thức sau: 

$$\text{SE}(\hat{\beta}_0)^2 = \sigma^2 \left[ \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right], \quad \text{SE}(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2},$$

trong đó $\sigma^2 = \text{Var}(\epsilon)$. Để các công thức này hoàn toàn hợp lệ, chúng ta cần giả định rằng các sai số $\epsilon_i$ cho mỗi quan sát có chung phương sai $\sigma^2$ và không có tương quan. Điều này rõ ràng là không đúng trong Hình 3.1, nhưng công thức vẫn tỏ ra là một phép xấp xỉ tốt. Lưu ý trong công thức rằng $\text{SE}(\hat{\beta}_1)$ nhỏ hơn khi các $x_i$ dàn trải hơn; theo trực giác, chúng ta có nhiều _đòn bẩy (leverage)_ hơn để ước lượng một độ dốc khi trường hợp này xảy ra. Chúng ta cũng thấy rằng $\text{SE}(\hat{\beta}_0)$ sẽ giống như $\text{SE}(\hat{\mu})$ nếu $\bar{x}$ bằng không (trong trường hợp đó $\hat{\beta}_0$ sẽ bằng $\bar{y}$). Nhìn chung, $\sigma^2$ là chưa biết, nhưng có thể được ước lượng từ dữ liệu. Ước lượng này của $\sigma$ được gọi là _sai số chuẩn phần dư (residual standard error)_, và được đưa ra bởi công thức phần dư $\text{RSE} = \sqrt{\text{RSS} / (n - 2)}$. Nói một cách nghiêm ngặt, khi $\sigma^2$ được ước lượng từ dữ liệu chuẩn chúng ta nên viết $\widehat{\text{SE}}(\hat{\beta}_1)$ để chỉ ra rằng một ước lượng đã được thực hiện, sai số nhưng để đơn giản hóa ký hiệu, chúng ta sẽ bỏ đi dấu "mũ" phụ này. 

sai số chuẩn 

Sai số chuẩn có thể được sử dụng để tính toán các _khoảng tin cậy (confidence intervals)_. Một khoảng tin cậy 95% độ tin cậy được định nghĩa là một phạm vi các giá trị sao cho với 95% khoảng xác suất, phạm vi sẽ chứa giá trị thực chưa biết của tham số. Phạm vi được định nghĩa theo giới hạn dưới và giới hạn trên được tính toán từ mẫu dữ liệu. Khoảng tin cậy 95% có tính chất sau: nếu chúng ta lấy các mẫu lặp lại và xây dựng khoảng tin cậy cho từng mẫu, 95% các khoảng sẽ chứa giá trị thực chưa biết của tham số. Đối với hồi quy tuyến tính, khoảng tin cậy 95% cho $\beta_1$ có dạng xấp xỉ như sau 

$$\hat{\beta}_1 \pm 2 \cdot \text{SE}(\hat{\beta}_1).$$

Nghĩa là, có khoảng 95% khả năng rằng khoảng 

$$[\hat{\beta}_1 - 2 \cdot \text{SE}(\hat{\beta}_1), \hat{\beta}_1 + 2 \cdot \text{SE}(\hat{\beta}_1)]$$

> 2Công thức này đúng với điều kiện là $n$ quan sát không có tương quan. 

3.1 Hồi quy tuyến tính đơn 67 

sẽ chứa giá trị thực của $\beta_1$.<sup>3</sup> Tương tự, một khoảng tin cậy cho $\beta_0$ có dạng xấp xỉ như sau 

$$\hat{\beta}_0 \pm 2 \cdot \text{SE}(\hat{\beta}_0).$$

Trong trường hợp dữ liệu quảng cáo, khoảng tin cậy 95% cho $\beta_0$ là $[6.130, 7.935]$ và khoảng tin cậy 95% cho $\beta_1$ là $[0.042, 0.053]$. Do đó, chúng ta có thể kết luận rằng khi không có bất kỳ quảng cáo nào, doanh số bán hàng, trung bình, sẽ rơi vào khoảng từ 6.130 đến 7.935 đơn vị. Hơn nữa, với mỗi mức tăng 1.000 đô la trong quảng cáo trên truyền hình, sẽ có mức tăng trung bình về doanh số bán hàng từ 42 đến 53 đơn vị. 

Sai số chuẩn cũng có thể được sử dụng để thực hiện các _kiểm định giả thuyết (hypothesis tests)_ trên giả thuyết các hệ số. Kiểm định giả thuyết phổ biến nhất liên quan đến việc kiểm định _giả thuyết không (null hypothesis)_ kiểm định 

kiểm định giả thuyết không 

$$H_0 : \text{There is no relationship between } X \text{ and } Y$$

so với _giả thuyết đối (alternative hypothesis)_ 

$$H_a : \text{There is some relationship between } X \text{ and } Y$$

giả thuyết đối 

Về mặt toán học, điều này tương ứng với việc kiểm định 

$$H_0 : \beta_1 = 0$$

so với 

$$H_a : \beta_1 \neq 0,$$

vì nếu $\beta_1 = 0$ thì mô hình (3.5) rút gọn thành $Y = \beta_0 + \epsilon$, và $X$ không có liên quan đến $Y$. Để kiểm định giả thuyết không, chúng ta cần xác định xem $\hat{\beta}_1$, ước lượng của chúng ta cho $\beta_1$, có đủ xa số không để chúng ta có thể tự tin rằng $\beta_1$ khác không hay không. Bao xa là đủ xa? Điều này dĩ nhiên phụ thuộc vào độ chính xác của $\hat{\beta}_1$—nghĩa là, nó phụ thuộc vào $\text{SE}(\hat{\beta}_1)$. Nếu $\text{SE}(\hat{\beta}_1)$ nhỏ, thì ngay cả những giá trị tương đối nhỏ của $\hat{\beta}_1$ cũng có thể cung cấp bằng chứng mạnh mẽ rằng $\beta_1 \neq 0$, và do đó có một mối quan hệ giữa $X$ và $Y$. Ngược lại, nếu $\text{SE}(\hat{\beta}_1)$ lớn, thì $\hat{\beta}_1$ phải có giá trị tuyệt đối lớn để chúng ta có thể bác bỏ giả thuyết không. Trong thực tế, chúng ta tính toán một _thống kê t (t-statistic)_, thống kê $t$ được đưa ra bởi 

$$t = \frac{\hat{\beta}_1 - 0}{\text{SE}(\hat{\beta}_1)},$$

> 3 _Xấp xỉ_ vì một số lý do. Phương trình 3.10 dựa trên giả định rằng các sai số tuân theo phân phối Gauss. Ngoài ra, hệ số 2 ở trước số hạng $\text{SE}(\hat{\beta}_1)$ sẽ thay đổi một chút tùy thuộc vào số lượng quan sát $n$ trong hồi quy tuyến tính. Để chính xác, thay vì số 2, (3.10) nên chứa phân vị 97,5% của một phân phối $t$ với $n-2$ bậc tự do. Chi tiết về cách tính toán khoảng tin cậy 95% một cách chính xác trong `R` sẽ được cung cấp ở phần sau của chương này. 

68 3. Hồi quy tuyến tính 

||Hệ số|Sai số chuẩn|Thống kê _t_|_p_-value|
|---|---|---|---|---|
|`Intercept`|7.0325|0.4578|15.36|_<_0.0001|
|`TV`|0.0475|0.0027|17.67|_<_0.0001|

**BẢNG 3.1.** _Đối với dữ liệu_ `Advertising` _, các hệ số của mô hình bình phương tối thiểu cho hồi quy của số lượng đơn vị được bán theo ngân sách quảng cáo TV. Mức tăng 1.000 đô la trong ngân sách quảng cáo TV có liên quan đến mức tăng doanh số bán hàng khoảng 50 đơn vị. (Nhớ lại rằng biến_ `sales` _được tính bằng hàng nghìn đơn vị, và biến_ `TV` _được tính bằng hàng nghìn đô la.)_ 

đo lường số lượng độ lệch chuẩn mà $\hat{\beta}_1$ cách biệt so với 0. Nếu thực sự không có mối quan hệ nào giữa $X$ và $Y$, thì chúng ta kỳ vọng rằng (3.14) sẽ có một phân phối $t$ với $n - 2$ bậc tự do. Phân phối $t$ có hình chuông và với các giá trị của $n$ lớn hơn khoảng 30, nó khá giống với phân phối chuẩn tiêu chuẩn. Do đó, việc tính toán xác suất quan sát được bất kỳ số nào bằng $|t|$ hoặc lớn hơn về giá trị tuyệt đối, giả sử $\beta_1 = 0$, là một vấn đề đơn giản. Chúng ta gọi xác suất này là _giá trị p (p-value)_. Nói một cách sơ lược, chúng ta diễn giải giá trị $p$ như sau: một giá trị $p$ nhỏ giá trị $p$ chỉ ra rằng không có khả năng quan sát được một mối liên hệ đáng kể như vậy giữa biến dự báo và biến phản hồi do ngẫu nhiên, khi không có bất kỳ mối liên hệ thực sự nào giữa biến dự báo và biến phản hồi. Do đó, nếu chúng ta thấy một giá trị $p$ nhỏ, thì chúng ta có thể suy luận rằng có một mối liên hệ giữa biến dự báo và biến phản hồi. Chúng ta _bác bỏ giả thuyết không_—nghĩa là, chúng ta tuyên bố một mối quan hệ tồn tại giữa $X$ và $Y$—nếu giá trị $p$ đủ nhỏ. Các ngưỡng giới hạn giá trị $p$ điển hình để bác bỏ giả thuyết không là 5% hoặc 1%, mặc dù chủ đề này sẽ được khám phá chi tiết hơn nhiều trong Chương 13. Khi $n = 30$, các ngưỡng này tương ứng với thống kê $t$ (3.14) khoảng 2 và 2.75, tương ứng. 

Bảng 3.1 cung cấp chi tiết về mô hình bình phương tối thiểu cho hồi quy của số lượng đơn vị được bán theo ngân sách quảng cáo TV đối với dữ liệu `Advertising`. Lưu ý rằng các hệ số cho $\hat{\beta}_0$ và $\hat{\beta}_1$ là rất lớn so với sai số chuẩn của chúng, do đó các thống kê $t$ cũng lớn; xác suất nhìn thấy các giá trị như vậy nếu $H_0$ đúng là gần như bằng không. Do đó chúng ta có thể kết luận rằng $\beta_0 \neq 0$ và $\beta_1 \neq 0$.<sup>4</sup>


### _3.1.3 Đánh giá Độ Chính xác của Mô hình_

Một khi chúng ta đã bác bỏ giả thuyết không (3.12) để ủng hộ giả thuyết thay thế (3.13), thật tự nhiên khi muốn định lượng _mức độ mà mô hình khớp với dữ liệu_. Chất lượng của một sự khớp hồi quy tuyến tính (linear regression fit) thường được đánh giá

> 4Trong Bảng 3.1, một _p_-value nhỏ cho hệ số chặn (intercept) chỉ ra rằng chúng ta có thể bác bỏ giả thuyết không rằng _β_ 0 = 0, và một _p_-value nhỏ cho `TV` chỉ ra rằng chúng ta có thể bác bỏ giả thuyết không rằng _β_ 1 = 0. Bác bỏ giả thuyết không sau cho phép chúng ta kết luận rằng có một mối quan hệ giữa `TV` và `sales`. Bác bỏ giả thuyết trước cho phép chúng ta kết luận rằng khi không có chi tiêu cho `TV`, `sales` là khác không.

3.1 Hồi quy Tuyến tính Đơn giản (Simple Linear Regression) 69

_R_<sup>2</sup>

|Đại lượng (Quantity)|Giá trị (Value)|
|---|---|
|Sai số chuẩn thặng dư (Residual standard error)|3.26|
|_R_<sup>2</sup>|0.612|
|_F_-statistic|312.1|



**BẢNG 3.2.** _Đối với dữ liệu_ `Advertising` _, thông tin thêm về mô hình bình phương tối thiểu (least squares model) cho hồi quy của số lượng đơn vị bán được theo ngân sách quảng cáo trên TV._

sử dụng hai đại lượng có liên quan: _sai số chuẩn thặng dư (residual standard error - RSE)_ và thống kê _R_<sup>2</sup>.

Bảng 3.2 hiển thị RSE, thống kê _R_<sup>2</sup>, và _F_-statistic (sẽ được mô tả trong Phần 3.2.2) cho hồi quy tuyến tính của số lượng đơn vị bán được theo ngân sách quảng cáo trên TV.

#### Sai số Chuẩn Thặng dư (Residual Standard Error)

Nhớ lại từ mô hình (3.5) rằng đi kèm với mỗi quan sát là một số hạng sai số _ϵ_. Do sự hiện diện của các số hạng sai số này, ngay cả khi chúng ta biết đường hồi quy thực sự (tức là ngay cả khi _β_ 0 và _β_ 1 đã được biết), chúng ta cũng sẽ không thể dự đoán hoàn hảo _Y_ từ _X_. RSE là một ước lượng của độ lệch chuẩn của _ϵ_. Nói một cách đại khái, đó là lượng trung bình mà biến phản hồi (response) sẽ chệch khỏi đường hồi quy thực sự. Nó được tính toán bằng cách sử dụng công thức


![](images/chapter_3.pdf-0011-08.png)


Lưu ý rằng RSS đã được định nghĩa trong Phần 3.1.1, và được cho bởi công thức


![](images/chapter_3.pdf-0011-10.png)


Trong trường hợp của dữ liệu quảng cáo, chúng ta thấy từ đầu ra của hồi quy tuyến tính trong Bảng 3.2 rằng RSE là 3 _._ 26. Nói cách khác, doanh số thực tế (actual sales) ở mỗi thị trường chệch khỏi đường hồi quy thực sự khoảng 3 _,_ 260 đơn vị, tính trung bình. Một cách khác để nghĩ về điều này là ngay cả khi mô hình là chính xác và giá trị thực sự của các hệ số chưa biết _β_ 0 và _β_ 1 được biết chính xác, bất kỳ dự đoán nào về doanh số dựa trên quảng cáo truyền hình (TV advertising) vẫn sẽ sai lệch đi khoảng 3 _,_ 260 đơn vị tính trung bình. Tất nhiên, việc 3 _,_ 260 đơn vị có phải là một sai số dự đoán có thể chấp nhận được hay không phụ thuộc vào bối cảnh của bài toán. Trong tập dữ liệu quảng cáo, giá trị trung bình của `sales` trên tất cả các thị trường là khoảng 14 _,_ 000 đơn vị, và do đó phần trăm sai số là 3 _,_ 260 _/_ 14 _,_ 000 = 23 %.

RSE được coi là một thước đo về sự _chưa khớp_ (lack of fit) của mô hình (3.5) với dữ liệu. Nếu các dự đoán thu được bằng cách sử dụng mô hình rất gần với các giá trị kết quả thực sự—tức là, nếu _yi ≈ yi_ ˆ cho _i_ = 1 _, . . . , n_—thì (3.15) sẽ nhỏ, và chúng ta có thể kết luận rằng mô hình khớp với dữ liệu rất tốt. Mặt 

70 3. Hồi quy Tuyến tính (Linear Regression)

khác, nếu _y_ ˆ _i_ rất xa so với _yi_ đối với một hoặc nhiều quan sát, thì RSE có thể khá lớn, chỉ ra rằng mô hình không khớp với dữ liệu tốt.

#### Thống kê _R_<sup>2</sup>

RSE cung cấp một thước đo tuyệt đối về sự chưa khớp của mô hình (3.5) với dữ liệu. Nhưng vì nó được đo bằng các đơn vị của _Y_, không phải lúc nào cũng rõ ràng thế nào cấu thành một RSE tốt. Thống kê _R_<sup>2</sup> cung cấp một thước đo độ khớp thay thế. Nó có dạng của một _tỷ lệ_—tỷ lệ phương sai được giải thích—và do đó nó luôn luôn nhận một giá trị giữa 0 và 1, và độc lập với thang đo của _Y_.

Để tính _R_<sup>2</sup>, chúngúng ta sử dụng công thức


![](images/chapter_3.pdf-0012-05.png)


¯ trong đó TSS =<sup></sup> ( _yi − y_ )<sup>2</sup> là _tổng bình phương toàn phần (total sum of squares)_, và RSS được định nghĩa trong (3.16). TSS đo lường tổng phương sai (total variance) trong biến phản hồi _Y_, và có thể được coi là lượng biến thiên vốn có trong biến phản hồi trước khi hồi quy được thực hiện. Ngược lại, RSS đo lường lượng biến thiên còn lại chưa được giải thích sau khi thực hiện hồi quy. Do đó, TSS _−_ RSS đo lường lượng biến thiên trong biến phản hồi được giải thích (hoặc bị loại bỏ) bằng cách thực hiện hồi quy, và _R_<sup>2</sup> đo lường _tỷ lệ biến thiên trong Y có thể được giải thích bằng cách sử dụng X_. Một thống kê _R_<sup>2</sup> gần bằng 1 chỉ ra rằng một tỷ lệ lớn của sự biến thiên trong biến phản hồi được giải thích bởi hồi quy. Một con số gần 0 chỉ ra rằng hồi quy không giải thích được nhiều sự biến thiên trong biến phản hồi; điều này có thể xảy ra vì mô hình tuyến tính sai, hoặc phương sai sai số _σ_<sup>2</sup> cao, hoặc cả hai. Trong Bảng 3.2, _R_<sup>2</sup> là 0 _._ 61, và do đó chỉ dưới hai phần ba sự biến thiên trong `sales` được giải thích bởi một hồi quy tuyến tính theo `TV`.

Thống kê _R_<sup>2</sup> (3.17) có một lợi thế về mặt diễn giải so với RSE (3.15), bởi vì không giống như RSE, nó luôn nằm trong khoảng từ 0 đến 1. Tuy nhiên, vẫn có thể khó để xác định thế nào là một giá trị _R_<sup>2</sup> _tốt_, và nói chung, điều này sẽ phụ thuộc vào ứng dụng. Ví dụ, trong một số bài toán vật lý, chúng ta có thể biết rằng dữ liệu thực sự đến từ một mô hình tuyến tính với một sai số thặng dư nhỏ. Trong trường hợp này, chúng ta sẽ kỳ vọng thấy một giá trị _R_<sup>2</sup> cực kỳ gần với 1, và một giá trị _R_<sup>2</sup> nhỏ hơn đáng kể có thể chỉ ra một vấn đề nghiêm trọng với thí nghiệm mà trong đó dữ liệu được tạo ra. Mặt khác, trong các ứng dụng điển hình trong sinh học, tâm lý học, tiếp thị, và các lĩnh vực khác, mô hình tuyến tính (3.5) tốt nhất cũng chỉ là một xấp xỉ cực kỳ thô cho dữ liệu, và các sai số thặng dư do các yếu tố chưa được đo lường khác thường rất lớn. Trong bối cảnh này, chúng ta sẽ chỉ kỳ vọng một tỷ lệ rất nhỏ của phương sai trong biến phản hồi được giải thích bởi biến dự báo, và một giá trị _R_<sup>2</sup> thấp hơn 0 _._ 1 có thể là thực tế hơn!

3.2 Hồi quy Tuyến tính Bội (Multiple Linear Regression) 71

Thống kê _R_<sup>2</sup> là một thước đo của mối quan hệ tuyến tính giữa _X_ và _Y_. Nhớ lại rằng _tương quan (correlation)_, được định nghĩa là


![](images/chapter_3.pdf-0013-03.png)


cũng là một thước đo của mối quan hệ tuyến tính giữa _X_ và _Y_.<sup>5</sup> Điều này gợi ý rằng chúng ta có thể sử dụng _r_ = Cor( _X, Y_ ) thay vì _R_<sup>2</sup> để đánh giá độ khớp của mô hình tuyến tính. Thực tế, có thể chỉ ra rằng trong bối cảnh hồi quy tuyến tính đơn giản, _R_<sup>2</sup> = _r_<sup>2</sup>. Nói cách khác, bình phương tương quan và thống kê _R_<sup>2</sup> là giống hệt nhau. Tuy nhiên, trong phần tiếp theo chúng ta sẽ thảo luận về bài toán hồi quy tuyến tính bội, trong đó chúng ta sử dụng nhiều biến dự báo đồng thời để dự đoán biến phản hồi. Khái niệm tương quan giữa các biến dự báo và biến phản hồi không tự động mở rộng sang bối cảnh này, vì tương quan định lượng sự liên kết giữa một cặp biến duy nhất chứ không phải giữa một số lượng biến lớn hơn. Chúng ta sẽ thấy rằng _R_<sup>2</sup> lấp đầy vai trò này.

## 3.2 Hồi quy Tuyến tính Bội (Multiple Linear Regression)

Hồi quy tuyến tính đơn giản là một phương pháp hữu ích để dự đoán một biến phản hồi dựa trên một biến dự báo duy nhất. Tuy nhiên, trong thực tế chúng ta thường có nhiều hơn một biến dự báo. Ví dụ, trong dữ liệu `Advertising`, chúng ta đã kiểm tra mối quan hệ giữa doanh số và quảng cáo trên TV. Chúng ta cũng có dữ liệu cho số tiền chi tiêu quảng cáo trên đài phát thanh (radio) và trên báo chí (newspaper), và chúng ta có thể muốn biết liệu một trong hai phương tiện này có liên kết với doanh số hay không. Làm thế nào chúng ta có thể mở rộng phân tích dữ liệu quảng cáo của mình để dung nạp (accommodate) hai biến dự báo bổ sung này?

Một tùy chọn là chạy ba hồi quy tuyến tính đơn giản riêng biệt, mỗi hồi quy sử dụng một phương tiện quảng cáo khác nhau như một biến dự báo. Ví dụ, chúng ta có thể khớp một hồi quy tuyến tính đơn giản để dự đoán doanh số dựa trên số tiền chi cho quảng cáo trên đài phát thanh. Kết quả được hiển thị trong Bảng 3.3 (bảng trên). Chúng ta nhận thấy rằng một sự gia tăng $1 _,_ 000 trong chi tiêu cho quảng cáo trên đài phát thanh có liên kết với một sự gia tăng doanh số khoảng 203 đơn vị. Bảng 3.3 (bảng dưới) chứa các hệ số bình phương tối thiểu cho một hồi quy tuyến tính đơn giản của doanh số theo ngân sách quảng cáo trên báo chí. Một sự gia tăng $1 _,_ 000 trong ngân sách quảng cáo trên báo chí có liên kết với một sự gia tăng doanh số khoảng 55 đơn vị.

Tuy nhiên, cách tiếp cận khớp một mô hình hồi quy tuyến tính đơn giản riêng biệt cho mỗi biến dự báo không hoàn toàn thỏa đáng. Trước hết, không rõ làm thế nào để đưa ra một dự đoán duy nhất về doanh số khi cho trước ba ngân sách phương tiện quảng cáo, vì mỗi ngân sách được liên kết với một phương trình hồi quy riêng biệt.

> 5Chúng tôi lưu ý rằng trên thực tế, vế phải của (3.18) là tương quan mẫu; do đó, sẽ đúng hơn nếu viết Cor( _X, Y_ ); tuy nhiên, chúng tôi bỏ qua dấu "mũ" (hat) để dễ ký hiệu.

72 3. Hồi quy Tuyến tính (Linear Regression)

Hồi quy đơn giản của `sales` theo `radio`

||Hệ số (Coefcient)|Sai số chuẩn (Std. error)|_t_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|9.312|0.563|16.54|_<_0_._0001|
|`radio`|0.203|0.020|9.92|_<_0_._0001|



Hồi quy đơn giản của `sales` theo `newspaper`

||Hệ số (Coefcient)|Sai số chuẩn (Std. error)|_t_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|12.351|0.621|19.88|_<_0_._0001|
|`newspaper`|0.055|0.017|3.30|0_._00115|



**BẢNG 3.3.** _Các mô hình hồi quy tuyến tính đơn giản bổ sung cho dữ liệu_ `Advertising` _. Các hệ số của mô hình hồi quy tuyến tính đơn giản cho số lượng đơn vị bán được theo_ Trên: _ngân sách quảng cáo trên đài phát thanh và_ Dưới: _ngân sách quảng cáo trên báo chí. Một sự gia tăng $_ 1 _,_ 000 _trong chi tiêu cho quảng cáo trên đài phát thanh có liên kết với một sự gia tăng trung bình về doanh số khoảng 203 đơn vị, trong khi sự gia tăng tương tự trong chi tiêu cho quảng cáo trên báo chí có liên kết với một sự gia tăng trung bình về doanh số khoảng 55 đơn vị. (Lưu ý rằng biến_ `sales` _tính bằng đơn vị hàng ngàn, và các biến_ `radio` _và_ `newspaper` _tính bằng đơn vị hàng ngàn đô la.)_

Thứ hai, mỗi phương trình trong ba phương trình hồi quy bỏ qua hai phương tiện còn lại trong việc hình thành các ước lượng cho các hệ số hồi quy. Chúng ta sẽ sớm thấy rằng nếu các ngân sách phương tiện tương quan với nhau trong 200 thị trường trong tập dữ liệu của chúng ta, thì điều này có thể dẫn đến những ước lượng rất sai lệch về sự liên kết giữa mỗi ngân sách phương tiện và doanh số.

Thay vì khớp một mô hình hồi quy tuyến tính đơn giản riêng biệt cho mỗi biến dự báo, một cách tiếp cận tốt hơn là mở rộng mô hình hồi quy tuyến tính đơn giản (3.5) để nó có thể trực tiếp dung nạp nhiều biến dự báo. Chúng ta có thể làm điều này bằng cách gán cho mỗi biến dự báo một hệ số góc (slope coefficient) riêng biệt trong một mô hình duy nhất. Nói chung, giả sử rằng chúng ta có _p_ biến dự báo phân biệt. Khi đó mô hình hồi quy tuyến tính bội có dạng


![](images/chapter_3.pdf-0014-08.png)


trong đó _Xj_ đại diện cho biến dự báo thứ _j_ và _βj_ định lượng sự liên kết giữa biến đó và biến phản hồi. Chúng ta diễn giải _βj_ là tác động _trung bình_ lên _Y_ của việc tăng một đơn vị trong _Xj_, _khi giữ cố định tất cả các biến dự báo khác_. Trong ví dụ quảng cáo, (3.19) trở thành


![](images/chapter_3.pdf-0014-10.png)


### _3.2.1 Ước lượng các Hệ số Hồi quy_

Giống như trường hợp trong bối cảnh hồi quy tuyến tính đơn giản, các hệ số hồi quy _β_ 0 _, β_ 1 _, . . . , βp_ trong (3.19) là chưa biết, và phải được ước lượng. Cho các 

3.2 Hồi quy Tuyến tính Bội (Multiple Linear Regression) 73

ước lượng _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, . . . , β_<sup>ˆ</sup> _p_, chúng ta có thể đưa ra các dự đoán bằng cách sử dụng công thức


![](images/chapter_3.pdf-0015-02.png)


Các tham số được ước lượng bằng cách sử dụng cùng một phương pháp bình phương tối thiểu mà chúng ta đã thấy trong bối cảnh của hồi quy tuyến tính đơn giản. Chúng ta chọn _β_ 0 _, β_ 1 _, . . . , βp_ để giảm thiểu tổng bình phương các phần dư (sum of squared residuals)


![](images/chapter_3.pdf-0015-04.png)


Các giá trị _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, . . . , β_<sup>ˆ</sup> _p_ làm giảm thiểu (3.22) là các ước lượng hệ số hồi quy bình phương tối thiểu bội (multiple least squares regression coefficient estimates). Không giống như các ước lượng hồi quy tuyến tính đơn giản được cho trong (3.4), các ước lượng hệ số hồi quy bội có dạng hơi phức tạp nên dễ được biểu diễn nhất bằng cách sử dụng đại số ma trận. Vì lý do này, chúng tôi không cung cấp chúng ở đây. Bất kỳ gói phần mềm thống kê nào cũng có thể được sử dụng để tính toán các ước lượng hệ số này, và sau này trong chương này, chúng tôi sẽ chỉ ra cách có thể thực hiện điều này trong `R`. Hình 3.4 minh họa một ví dụ về độ khớp bình phương tối thiểu cho một tập dữ liệu đồ chơi với _p_ = 2 biến dự báo.

Bảng 3.4 hiển thị các ước lượng hệ số hồi quy bội khi ngân sách quảng cáo trên TV, đài phát thanh và báo chí được sử dụng để dự đoán doanh số sản phẩm bằng cách sử dụng dữ liệu `Advertising`. Chúng ta diễn giải các kết quả này như sau: với một lượng quảng cáo nhất định trên TV và báo chí, chi tiêu thêm $1 _,_ 000 cho quảng cáo trên đài phát thanh có liên kết với khoảng 189 đơn vị doanh số bổ sung. So sánh các ước lượng hệ số này với các ước lượng được hiển thị trong Bảng 3.1 và 3.3, chúng ta nhận thấy rằng các ước lượng hệ số hồi quy bội cho `TV` và `radio` khá giống với các ước lượng hệ số hồi quy tuyến tính đơn giản. Tuy nhiên, trong khi ước lượng hệ số hồi quy `newspaper` trong Bảng 3.3 khác không một cách có ý nghĩa, thì ước lượng hệ số cho `newspaper` trong mô hình hồi quy bội lại gần bằng không, và _p_-value tương ứng không còn có ý nghĩa nữa, với giá trị khoảng 0 _._ 86. Điều này minh họa rằng các hệ số hồi quy đơn giản và bội có thể khá khác nhau. Sự khác biệt này xuất phát từ thực tế là trong trường hợp hồi quy đơn giản, số hạng góc đại diện cho sự gia tăng trung bình trong doanh số sản phẩm có liên kết với sự gia tăng $1 _,_ 000 trong quảng cáo trên báo chí, bỏ qua các biến dự báo khác như `TV` và `radio`. Ngược lại, trong bối cảnh hồi quy bội, hệ số cho `newspaper` đại diện cho sự gia tăng trung bình trong doanh số sản phẩm có liên kết với việc tăng chi tiêu báo chí thêm $1 _,_ 000 trong khi giữ nguyên `TV` và `radio`.

Liệu việc hồi quy bội gợi ý không có mối quan hệ nào giữa `sales` và `newspaper` trong khi hồi quy tuyến tính đơn giản lại ngụ ý 

74 3. Hồi quy Tuyến tính (Linear Regression)


![](images/chapter_3.pdf-0016-01.png)


**HÌNH 3.4.** _Trong một không gian ba chiều, với hai biến dự báo và một biến phản hồi, đường hồi quy bình phương tối thiểu trở thành một mặt phẳng. Mặt phẳng được chọn để làm giảm thiểu tổng bình phương khoảng cách thẳng đứng giữa mỗi quan sát (được hiển thị bằng màu đỏ) và mặt phẳng._

điều ngược lại có hợp lý không? Thực tế là có. Hãy xem xét ma trận tương quan (correlation matrix) cho ba biến dự báo và biến phản hồi, được hiển thị trong Bảng 3.5. Lưu ý rằng tương quan giữa `radio` và `newspaper` là 0 _._ 35. Điều này chỉ ra rằng các thị trường có quảng cáo trên báo chí cao cũng có xu hướng có quảng cáo trên đài phát thanh cao. Bây giờ giả sử rằng hồi quy bội là chính xác và quảng cáo trên báo chí không có liên kết với doanh số, nhưng quảng cáo trên đài phát thanh có liên kết với doanh số. Khi đó, tại các thị trường nơi chúng ta chi nhiều hơn cho đài phát thanh, doanh số của chúng ta sẽ có xu hướng cao hơn, và như ma trận tương quan của chúng ta cho thấy, chúng bản cũng có xu hướng chi nhiều hơn cho quảng cáo trên báo chí ở những thị trường đó. Do đó, trong một hồi quy tuyến tính đơn giản chỉ kiểm tra `sales` so với 

||Hệ số (Coefcient)|Sai số chuẩn (Std. error)|_t_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|2.939|0.3119|9.42|_<_0_._0001|
|`TV`|0.046|0.0014|32.81|_<_0_._0001|
|`radio`|0.189|0.0086|21.89|_<_0_._0001|
|`newspaper`|_−_0.001|0.0059|_−_0.18|0_._8599|



**BẢNG 3.4.** _Đối với dữ liệu_ `Advertising` _, các ước lượng hệ số bình phương tối thiểu của hồi quy tuyến tính bội cho số lượng đơn vị bán được theo ngân sách quảng cáo trên TV, đài phát thanh, và báo chí._

3.2 Hồi quy Tuyến tính Bội (Multiple Linear Regression) 75

||`TV`|`radio`|`newspaper`|`sales`|
|---|---|---|---|---|
|`TV`|1.0000|0.0548|0.0567|0.7822|
|`radio`||1.0000|0.3541|0.5762|
|`newspaper`|||1.0000|0.2283|
|`sales`||||1.0000|



**BẢNG 3.5.** _Ma trận tương quan cho_ `TV` _,_ `radio` _,_ `newspaper` _, và_ `sales` _đối với dữ liệu_ `Advertising` _._

`newspaper`, chúng ta sẽ quan sát thấy rằng các giá trị cao hơn của `newspaper` có xu hướng có liên kết với các giá trị cao hơn của `sales`, mặc dù quảng cáo trên báo chí không liên kết trực tiếp với doanh số. Vì vậy, quảng cáo trên `newspaper` đóng vai trò là một vật thay thế (surrogate) cho quảng cáo trên `radio`; `newspaper` nhận được "sự ghi nhận" cho sự liên kết giữa `radio` và `sales`.

Kết quả hơi ngược trực giác này rất phổ biến trong nhiều tình huống thực tế. Hãy xem xét một ví dụ ngớ ngẩn để minh họa quan điểm này. Chạy một hồi quy về các cuộc tấn công của cá mập so với doanh số bán kem cho dữ liệu được thu thập tại một cộng đồng bãi biển nhất định trong một khoảng thời gian sẽ cho thấy một mối quan hệ đồng biến, tương tự như những gì được thấy giữa `sales` và `newspaper`. Tất nhiên, chưa có ai đề xuất rằng kem nên bị cấm ở các bãi biển để giảm các cuộc tấn công của cá mập. Trên thực tế, nhiệt độ cao hơn khiến nhiều người đến bãi biển hơn, từ đó dẫn đến doanh số bán kem cao hơn và nhiều cuộc tấn công của cá mập hơn. Một hồi quy bội của các cuộc tấn công của cá mập lên doanh số bán kem và nhiệt độ tiết lộ rằng, như trực giác ngụ ý, doanh số bán kem không còn là một biến dự báo có ý nghĩa sau khi điều chỉnh theo nhiệt độ.

### _3.2.2 Một số Câu hỏi Quan trọng_

Khi chúng ta thực hiện hồi quy tuyến tính bội, chúng ta thường quan tâm đến việc trả lời một vài câu hỏi quan trọng.

1. _Có ít nhất một trong các biến dự báo X_ 1 _, X_ 2 _, . . . , Xp có ích trong việc dự đoán biến phản hồi không?_

2. _Tất cả các biến dự báo có giúp giải thích Y không, hay chỉ một tập con các biến dự báo có ích?_

3. _Mô hình khớp với dữ liệu tốt đến mức nào?_

4. _Với một tập các giá trị biến dự báo, chúng ta nên dự đoán giá trị phản hồi nào, và dự đoán của chúng ta chính xác đến đâu?_

Bây giờ chúng ta lần lượt giải quyết từng câu hỏi này.

Câu hỏi 1: Có Mối quan hệ Nào Giữa Biến Phản hồi và Các Biến Dự báo Không?

Nhớ lại rằng trong bối cảnh hồi quy tuyến tính đơn giản, để xác định xem có mối quan hệ giữa biến phản hồi và biến dự báo hay không, chúng ta 

76 3. Hồi quy Tuyến tính (Linear Regression)

|Đại lượng (Quantity)|Giá trị (Value)|
|---|---|
|Sai số chuẩn thặng dư (Residual standard error)|1.69|
|_R_<sup>2</sup>|0.897|
|_F_-statistic|570|



**BẢNG 3.6.** _Thông tin thêm về mô hình bình phương tối thiểu cho hồi quy của số lượng đơn vị bán được theo ngân sách quảng cáo trên TV, báo chí, và đài phát thanh trong dữ liệu_ `Advertising` _. Thông tin khác về mô hình này đã được hiển thị trong Bảng 3.4._

có thể đơn giản kiểm tra xem _β_ 1 = 0. Trong bối cảnh hồi quy bội với _p_ biến dự báo, chúng ta cần hỏi xem liệu tất cả các hệ số hồi quy có bằng không hay không, tức là liệu _β_ 1 = _β_ 2 = _· · ·_ = _βp_ = 0. Giống như trong bối cảnh hồi quy tuyến tính đơn giản, chúng ta sử dụng một kiểm định giả thuyết (hypothesis test) để trả lời câu hỏi này. Chúng ta kiểm định giả thuyết không,


![](images/chapter_3.pdf-0018-04.png)


chống lại giả thuyết thay thế


![](images/chapter_3.pdf-0018-06.png)


Kiểm định giả thuyết này được thực hiện bằng cách tính toán _F-statistic_,


![](images/chapter_3.pdf-0018-09.png)


¯ trong đó, cũng như hồi quy tuyến tính đơn giản, TSS =<sup></sup> ( _yi − y_ )<sup>2</sup> và RSS = ˆ 2 ( _yi − yi_ ). Nếu các giả định của mô hình tuyến tính là chính xác, người ta có thể chỉ ra rằng


![](images/chapter_3.pdf-0018-11.png)


và rằng, với điều kiện _H_ 0 đúng,


![](images/chapter_3.pdf-0018-13.png)


Do đó, khi không có mối quan hệ nào giữa biến phản hồi và các biến dự báo, người ta sẽ kỳ vọng _F_-statistic nhận một giá trị gần bằng 1. Mặt khác, nếu _Ha_ đúng, thì _E{_ (TSS _−_ RSS) _/p} > σ_<sup>2</sup>, vì vậy chúng ta kỳ vọng _F_ lớn hơn 1.

_F_-statistic cho mô hình hồi quy tuyến tính bội thu được bằng cách hồi quy `sales` theo `radio`, `TV`, và `newspaper` được hiển thị trong Bảng 3.6. Trong ví dụ này, _F_-statistic là 570. Vì con số này lớn hơn rất nhiều so với 1, nó cung cấp bằng chứng thuyết phục chống lại giả thuyết không _H_ 0. Nói cách khác, _F_-statistic lớn gợi ý rằng ít nhất một trong các phương tiện quảng cáo phải có liên quan đến `sales`. Tuy nhiên, điều gì sẽ xảy ra nếu _F_-statistic gần hơn với 1? _F_-statistic cần lớn đến mức nào trước khi chúng ta có thể bác bỏ _H_ 0 và kết luận rằng có một mối quan hệ? Hóa ra câu trả lời phụ thuộc vào các giá trị của _n_ và _p_. Khi _n_ lớn, một _F_-statistic chỉ lớn hơn 1 một chút vẫn có thể cung cấp bằng chứng chống lại _H_ 0. Ngược lại, 

3.2 Hồi quy Tuyến tính Bội (Multiple Linear Regression) 77

một _F_-statistic lớn hơn là cần thiết để bác bỏ _H_ 0 nếu _n_ nhỏ. Khi _H_ 0 đúng và các sai số _ϵi_ có phân phối chuẩn, _F_-statistic tuân theo một phân phối _F_.<sup>6</sup> Với bất kỳ giá trị nhất định nào của _n_ và _p_, bất kỳ gói phần mềm thống kê nào cũng có thể được sử dụng để tính _p_-value được liên kết với _F_-statistic bằng cách sử dụng phân phối này. Dựa trên _p_-value này, chúng ta có thể xác định xem có nên bác bỏ _H_ 0 hay không. Đối với dữ liệu quảng cáo, _p_-value được liên kết với _F_-statistic trong Bảng 3.6 về cơ bản là bằng không, vì vậy chúng ta có bằng chứng cực kỳ mạnh mẽ rằng ít nhất một trong các phương tiện truyền thông có liên kết với việc tăng `sales`.

Trong (3.23) chúng ta đang kiểm định _H_ 0 rằng tất cả các hệ số đều bằng không. Đôi khi chúng ta muốn kiểm định rằng một tập con cụ thể gồm _q_ hệ số bằng không. Điều này tương ứng với một giả thuyết không


![](images/chapter_3.pdf-0019-03.png)


trong đó để thuận tiện, chúng tôi đã đặt các biến được chọn để loại bỏ ở cuối danh sách. Trong trường hợp này, chúng ta khớp một mô hình thứ hai sử dụng tất cả các biến _ngoại trừ_ _q_ biến cuối cùng đó. Giả sử rằng tổng bình phương phần dư cho mô hình đó là RSS0. Khi đó, _F_-statistic thích hợp là


![](images/chapter_3.pdf-0019-05.png)


Lưu ý rằng trong Bảng 3.4, đối với mỗi biến dự báo riêng lẻ, một _t_-statistic và một _p_-value đã được báo cáo. Chúng cung cấp thông tin về việc liệu mỗi biến dự báo riêng lẻ có liên quan đến biến phản hồi hay không, sau khi điều chỉnh cho các biến dự báo khác. Hóa ra mỗi kiểm định này hoàn toàn tương đương<sup>7</sup> với kiểm định _F_ bỏ sót một biến duy nhất đó khỏi mô hình, để lại tất cả các biến khác—tức là _q_ =1 trong (3.24). Vì vậy, nó báo cáo tác động _từng phần (partial effect)_ của việc thêm biến đó vào mô hình. Ví dụ, như chúng ta đã thảo luận trước đó, các _p_-value này chỉ ra rằng `TV` và `radio` có liên quan đến `sales`, nhưng không có bằng chứng nào cho thấy `newspaper` có liên kết với `sales`, khi `TV` và `radio` được giữ cố định.

Với các _p_-value riêng lẻ này cho mỗi biến, tại sao chúng ta cần xem xét tổng thể _F_-statistic? Rốt cuộc, có vẻ hợp lý rằng nếu bất kỳ một trong các _p_-value cho các biến riêng lẻ rất nhỏ, thì _ít nhất một trong các biến dự báo có liên quan đến biến phản hồi_. Tuy nhiên, logic này có sai sót, đặc biệt khi số lượng biến dự báo _p_ là lớn.

Ví dụ, hãy xem xét một ví dụ trong đó _p_ = 100 và _H_ 0 : _β_ 1 = _β_ 2 = _· · ·_ = _βp_ = 0 là đúng, vì vậy thực sự không có biến nào liên kết với biến phản hồi. Trong tình huống này, khoảng 5 % các _p_-value được liên kết với mỗi biến (thuộc loại được hiển thị trong Bảng 3.4) sẽ dưới 0 _._ 05 một cách ngẫu nhiên. Nói cách khác, chúng ta kỳ vọng sẽ thấy khoảng năm _p_-value _nhỏ_ ngay cả khi không có 

> 6Ngay cả khi các sai số không có phân phối chuẩn, _F_-statistic xấp xỉ tuân theo một phân phối _F_ với điều kiện cỡ mẫu _n_ lớn.

> 7Bình phương của mỗi _t_-statistic là _F_-statistic tương ứng.

78 3. Hồi quy Tuyến tính (Linear Regression)

bất kỳ sự liên kết thực sự nào giữa các biến dự báo và biến phản hồi.<sup>8</sup> Thực tế, rất có khả năng chúng ta sẽ quan sát thấy ít nhất một _p_-value dưới 0 _._ 05 một cách ngẫu nhiên! Do đó, nếu chúng ta sử dụng các _t_-statistics riêng lẻ và các _p_-value được liên kết để quyết định xem có bất kỳ sự liên kết nào giữa các biến và biến phản hồi hay không, thì có khả năng rất cao là chúng ta sẽ kết luận không chính xác rằng có một mối quan hệ. Tuy nhiên, _F_-statistic không gặp phải vấn đề này vì nó điều chỉnh cho số lượng biến dự báo. Do đó, nếu _H_ 0 đúng, chỉ có 5 % cơ hội _F_-statistic sẽ dẫn đến một _p_-value dưới 0 _._ 05, bất kể số lượng biến dự báo hay số lượng quan sát.

Cách tiếp cận sử dụng _F_-statistic để kiểm định bất kỳ sự liên kết nào giữa các biến dự báo và biến phản hồi hoạt động khi _p_ tương đối nhỏ, và chắc chắn nhỏ so với _n_. Tuy nhiên, đôi khi chúng ta có một số lượng biến rất lớn. Nếu _p > n_ thì có nhiều hệ số _βj_ để ước lượng hơn là số lượng quan sát dùng để ước lượng chúng. Trong trường hợp này, chúng ta thậm chí không thể khớp mô hình hồi quy tuyến tính bội bằng cách sử dụng bình phương tối thiểu, do đó không thể sử dụng _F_-statistic, và hầu hết các khái niệm khác mà chúng ta đã thấy cho đến nay trong chương này cũng vậy. Khi _p_ lớn, một số cách tiếp cận được thảo luận trong phần tiếp theo, chẳng hạn như _lựa chọn tiến (forward selection)_, có thể được sử dụng. Bối cảnh _chiều cao (high-dimensional)_ này được thảo luận chi tiết hơn trong Chương 6.

highdimensional


#### Hai: Quyết định các biến quan trọng

Như đã thảo luận trong phần trước, bước đầu tiên trong phân tích hồi quy bội là tính toán thống kê _F_ và kiểm tra _p_ -value tương ứng. Nếu chúng ta kết luận dựa trên _p_ -value đó rằng có ít nhất một trong các biến dự báo có liên quan đến biến phản hồi, thì điều tự nhiên là muốn biết _biến nào_ mới là thủ phạm! Chúng ta có thể xem xét các _p_ -value riêng lẻ như trong Bảng 3.4, nhưng như đã thảo luận (và sẽ được khám phá thêm trong Chương 13), nếu _p_ lớn, chúng ta có khả năng tạo ra một số khám phá sai lầm (false discoveries).

Có khả năng tất cả các biến dự báo đều có liên quan đến biến phản hồi, nhưng thông thường, biến phản hồi chỉ liên quan đến một tập con các biến dự báo. Nhiệm vụ xác định biến dự báo nào có liên quan đến biến phản hồi, để khớp (fit) một mô hình duy nhất chỉ bao gồm các biến dự báo đó, được gọi là _lựa chọn biến_ (variable selection). Vấn đề lựa chọn biến được nghiên cứu rộng rãi trong Chương 6, và do đó ở đây chúng tôi sẽ chỉ cung cấp một dàn ý ngắn gọn về một số phương pháp cổ điển.

selection

Lý tưởng nhất là, chúng ta muốn thực hiện lựa chọn biến bằng cách thử nhiều mô hình khác nhau, mỗi mô hình chứa một tập con khác nhau của các biến dự báo. Ví dụ, nếu _p_ = 2, thì chúng ta có thể xem xét bốn mô hình: (1) mô hình không chứa biến nào, (2) mô hình chỉ chứa _X_ 1, (3) mô hình chỉ chứa _X_ 2, và (4) mô hình chứa cả _X_ 1 và _X_ 2. Sau đó, chúng ta có thể chọn

> 8Điều này liên quan đến khái niệm quan trọng về _kiểm định đa lượng_ (multiple testing), là trọng tâm của Chương 13.

3.2 Multiple Linear Regression 79

mô hình _tốt nhất_ trong số tất cả các mô hình mà chúng ta đã xem xét. Làm thế nào để chúng ta xác định mô hình nào là tốt nhất? Có thể sử dụng nhiều thống kê khác nhau để đánh giá chất lượng của một mô hình. Chúng bao gồm thống kê _C_<sub>_p_</sub> của Mallow (Mallow's _C_<sub>_p_</sub>), _tiêu chuẩn thông tin Akaike_ (Akaike information criterion - AIC), _tiêu chuẩn thông tin Bayesian_ (Bayesian information criterion - BIC), và _R_<sup>2</sup> _điều chỉnh_ (adjusted _R_<sup>2</sup>). Những khái niệm này được thảo luận chi tiết hơn ở Chương 6. Chúng ta cũng có thể xác định mô hình nào là tốt nhất bằng cách vẽ đồ thị các đầu ra (outputs) của mô hình, chẳng hạn như phần dư (residuals), để tìm kiếm các mẫu (patterns).

Akaike information criterion Bayesian information criterion adjusted _R_<sup>2</sup>

Thật không may, có tổng cộng 2<sup>_p_</sup> mô hình chứa các tập con của _p_ biến. Điều này có nghĩa là ngay cả với _p_ ở mức vừa phải, việc thử nghiệm mọi tập con có thể có của các biến dự báo là không khả thi. Ví dụ, chúng ta đã thấy rằng nếu _p_ = 2, thì có 2<sup>2</sup> = 4 mô hình cần xem xét. Nhưng nếu _p_ = 30, thì chúng ta phải xem xét 2<sup>30</sup> = 1 _,_ 073 _,_ 741 _,_ 824 mô hình! Điều này là không thực tế. Do đó, trừ khi _p_ rất nhỏ, chúng ta không thể xem xét tất cả 2<sup>_p_</sup> mô hình, thay vào đó chúng ta cần một phương pháp tự động và hiệu quả để chọn một tập hợp các mô hình nhỏ hơn để xem xét. Có ba phương pháp tiếp cận cổ điển cho tác vụ này:

- _Lựa chọn tiến_ (Forward selection). Chúng ta bắt đầu với _mô hình null_ — một mô hình chứa hệ số chặn (intercept) nhưng không có biến dự báo nào. Sau đó, chúng ta khớp _p_ hồi quy tuyến tính đơn và thêm vào mô hình null biến dẫn đến tổng bình phương phần dư (RSS) thấp nhất. Tiếp theo, chúng ta thêm vào mô hình đó biến dẫn đến RSS thấp nhất cho mô hình hai biến mới. Cách tiếp cận này được tiếp tục cho đến khi thỏa mãn một quy tắc dừng nào đó.

selection null model

- _Lựa chọn lùi_ (Backward selection). Chúng ta bắt đầu với tất cả các biến trong mô hình, và loại bỏ biến có _p_ -value lớn nhất — nghĩa là biến ít có ý nghĩa thống kê nhất. Mô hình ( _p −_ 1) biến mới được khớp, và biến có _p_ -value lớn nhất tiếp tục bị loại bỏ. Quá trình này tiếp tục cho đến khi đạt đến một quy tắc dừng. Ví dụ, chúng ta có thể dừng lại khi tất cả các biến còn lại đều có _p_ -value dưới một ngưỡng nào đó.

- _Lựa chọn hỗn hợp_ (Mixed selection). Đây là sự kết hợp của lựa chọn tiến và lựa chọn lùi. Chúng ta bắt đầu với không có biến nào trong mô hình, và giống như lựa chọn tiến, chúng ta thêm biến cung cấp mức độ khớp (fit) tốt nhất. Chúng ta tiếp tục thêm lần lượt từng biến. Tất nhiên, như chúng ta đã lưu ý với ví dụ `Advertising`, các _p_ -value của các biến có thể trở nên lớn hơn khi các biến dự báo mới được thêm vào mô hình. Do đó, nếu tại bất kỳ thời điểm nào, _p_ -value của một trong các biến trong mô hình tăng vượt quá một ngưỡng nhất định, thì chúng ta loại bỏ biến đó khỏi mô hình. Chúng ta tiếp tục thực hiện các bước tiến và lùi này cho đến khi tất cả các biến trong mô hình đều có _p_ -value đủ thấp, và tất cả các biến nằm ngoài mô hình sẽ có _p_ -value lớn nếu được thêm vào mô hình.

   - selection

Lựa chọn lùi không thể được sử dụng nếu _p > n_ , trong khi lựa chọn tiến luôn có thể được sử dụng. Lựa chọn tiến là một phương pháp tham lam (greedy) và có thể bao gồm các biến ở giai đoạn đầu mà sau này trở nên dư thừa. Lựa chọn hỗn hợp có thể khắc phục được điều này.

80 3. Linear Regression

#### Ba: Mức độ khớp mô hình (Model Fit)

Hai trong số các độ đo số phổ biến nhất về mức độ khớp mô hình là RSE và _R_<sup>2</sup>, tỷ lệ phần trăm của phương sai được giải thích (fraction of variance explained). Các đại lượng này được tính toán và diễn giải theo cách tương tự như đối với hồi quy tuyến tính đơn.

Nhớ lại rằng trong hồi quy đơn, _R_<sup>2</sup> là bình phương của hệ số tương quan giữa biến phản hồi và biến dự báo. Trong hồi quy tuyến tính bội, hóa ra nó bằng Cor( _Y, Y_<sup>ˆ</sup> )<sup>2</sup>, bình phương của hệ số tương quan giữa biến phản hồi và mô hình tuyến tính được khớp; trên thực tế, một tính chất của mô hình tuyến tính được khớp là nó tối đa hóa hệ số tương quan này trong số tất cả các mô hình tuyến tính có thể có.

Một giá trị _R_<sup>2</sup> gần bằng 1 chỉ ra rằng mô hình giải thích được một phần lớn phương sai trong biến phản hồi. Ví dụ, chúng ta đã thấy trong Bảng 3.6 rằng đối với dữ liệu `Advertising`, mô hình sử dụng cả ba phương tiện quảng cáo để dự báo `sales` có _R_<sup>2</sup> là 0 _._ 8972. Mặt khác, mô hình chỉ sử dụng `TV` và `radio` để dự báo `sales` có giá trị _R_<sup>2</sup> là 0 _._ 89719. Nói cách khác, có một sự gia tăng _nhỏ_ trong _R_<sup>2</sup> nếu chúng ta thêm quảng cáo trên báo (newspaper) vào mô hình đã chứa quảng cáo trên TV và radio, mặc dù chúng ta đã thấy trước đó rằng _p_ -value của quảng cáo trên báo trong Bảng 3.4 là không có ý nghĩa thống kê (not significant). Hóa ra là _R_<sup>2</sup> sẽ luôn tăng khi có thêm các biến được thêm vào mô hình, ngay cả khi những biến đó chỉ liên quan yếu đến biến phản hồi. Điều này là do thực tế là việc thêm một biến khác luôn dẫn đến sự sụt giảm tổng bình phương phần dư (RSS) trên dữ liệu huấn luyện (mặc dù không nhất thiết là trên dữ liệu kiểm tra). Do đó, thống kê _R_<sup>2</sup>, vốn cũng được tính toán trên dữ liệu huấn luyện, bắt buộc phải tăng lên. Việc thêm quảng cáo trên báo vào mô hình chỉ chứa quảng cáo trên TV và radio dẫn đến mức tăng cực nhỏ trong _R_<sup>2</sup> cung cấp thêm bằng chứng cho thấy `newspaper` có thể bị loại bỏ khỏi mô hình. Về cơ bản, `newspaper` không cung cấp cải thiện thực sự nào cho mức độ khớp của mô hình trên các mẫu huấn luyện, và việc bao gồm nó có khả năng sẽ dẫn đến kết quả kém trên các mẫu kiểm tra độc lập do hiện tượng quá khớp (overfitting).

Ngược lại, mô hình chỉ chứa `TV` làm biến dự báo có _R_<sup>2</sup> là 0 _._ 61 (Bảng 3.2). Việc thêm `radio` vào mô hình dẫn đến sự cải thiện đáng kể trong _R_<sup>2</sup>. Điều này ngụ ý rằng một mô hình sử dụng chi tiêu cho TV và radio để dự báo doanh số bán hàng (sales) tốt hơn đáng kể so với mô hình chỉ sử dụng quảng cáo trên TV. Chúng ta có thể định lượng thêm sự cải thiện này bằng cách xem xét _p_ -value của hệ số `radio` trong một mô hình chỉ chứa `TV` và `radio` làm biến dự báo.

Mô hình chỉ chứa `TV` và `radio` làm biến dự báo có RSE là 1.681, và mô hình chứa thêm `newspaper` làm biến dự báo có RSE là 1.686 (Bảng 3.6). Trái lại, mô hình chỉ chứa `TV` có RSE là 3 _._ 26 (Bảng 3.2). Điều này củng cố kết luận trước đó của chúng ta rằng mô hình sử dụng chi tiêu cho TV và radio để dự báo doanh số bán hàng chính xác hơn nhiều (trên dữ liệu huấn luyện) so với mô hình chỉ sử dụng chi tiêu cho TV. Hơn nữa, với việc chi tiêu cho TV và radio đã được sử dụng làm biến dự báo, không có lý do gì để sử dụng thêm chi tiêu cho báo chí làm biến dự báo trong 

3.2 Multiple Linear Regression 81

![](images/chapter_3.pdf-0023-01.png)

**HÌNH 3.5.** _Đối với dữ liệu_ `Advertising` _, một mô hình hồi quy tuyến tính được khớp cho_ `sales` _sử dụng_ `TV` _và_ `radio` _làm biến dự báo. Từ mô hình của các phần dư, chúng ta có thể thấy rằng có một mối quan hệ phi tuyến tính rõ rệt trong dữ liệu. Các phần dư dương (những phần có thể nhìn thấy phía trên bề mặt) có xu hướng nằm dọc theo đường 45 độ, nơi ngân sách cho TV và Radio được phân chia đều. Các phần dư âm (hầu hết không nhìn thấy được) có xu hướng nằm xa đường này, nơi ngân sách bị lệch hơn._

mô hình. Độc giả tinh ý có thể thắc mắc làm thế nào RSE lại có thể tăng khi `newspaper` được thêm vào mô hình trong khi RSS bắt buộc phải giảm. Nói chung, RSE được định nghĩa là

![](images/chapter_3.pdf-0023-04.png)

sẽ rút gọn về (3.15) cho một hồi quy tuyến tính đơn. Do đó, các mô hình có nhiều biến hơn có thể có RSE cao hơn nếu mức giảm của RSS nhỏ so với mức tăng của _p_ .

Ngoài việc xem xét các thống kê RSE và _R_<sup>2</sup> vừa thảo luận, việc vẽ đồ thị dữ liệu cũng có thể hữu ích. Các tóm tắt bằng đồ họa có thể tiết lộ những vấn đề với mô hình mà không thể nhìn thấy từ các thống kê dạng số. Ví dụ, Hình 3.5 hiển thị một biểu đồ ba chiều của `TV` và `radio` so với `sales`. Chúng ta thấy rằng một số quan sát nằm phía trên và một số quan sát nằm phía dưới mặt phẳng hồi quy bình phương tối thiểu (least squares regression plane). Cụ thể, mô hình tuyến tính dường như đánh giá quá cao (overestimate) `sales` đối với các trường hợp mà hầu hết số tiền quảng cáo được chi tiêu độc quyền cho `TV` hoặc `radio`. Nó đánh giá thấp (underestimate) `sales` cho các trường hợp ngân sách được chia đều giữa hai phương tiện. Mô hình phi tuyến tính rõ rệt này cho thấy sự _cộng hưởng_ (synergy) hoặc _tương tác_ (interaction) giữa các phương tiện quảng cáo, theo đó việc kết hợp các phương tiện với nhau sẽ mang lại mức tăng doanh số lớn hơn so với việc sử dụng bất kỳ phương tiện đơn lẻ nào. Trong Mục 3.3.2, chúng ta sẽ thảo luận về việc mở rộng mô hình tuyến tính để điều chỉnh các hiệu ứng cộng hưởng như vậy thông qua việc sử dụng các số hạng tương tác (interaction terms).

82 3. Linear Regression

#### Bốn: Dự báo (Predictions)

Một khi chúng ta đã khớp mô hình hồi quy bội, việc áp dụng (3.21) để dự báo biến phản hồi _Y_ trên cơ sở một tập hợp các giá trị của các biến dự báo _X_ 1 _, X_ 2 _, . . . , Xp_ là hoàn toàn đơn giản. Tuy nhiên, có ba loại yếu tố không chắc chắn (uncertainty) liên quan đến dự báo này.

1. Các ước lượng hệ số _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, . . . , β_<sup>ˆ</sup> _p_ là các ước lượng cho _β_ 0 _, β_ 1 _, . . . , βp_ . Điều đó có nghĩa là, _mặt phẳng bình phương tối thiểu_

![](images/chapter_3.pdf-0024-04.png)

chỉ là một ước lượng cho _mặt phẳng hồi quy quần thể thực_

![](images/chapter_3.pdf-0024-06.png)

Sự không chính xác trong các ước lượng hệ số có liên quan đến _sai số có thể giảm thiểu_ (reducible error) từ Chương 2. Chúng ta có thể tính toán một _khoảng tin cậy_ (confidence interval) để xác định xem _Y_<sup>ˆ</sup> sẽ sát với _f_ ( _X_ ) đến mức nào.

2. Tất nhiên, trong thực tế, việc giả định một mô hình tuyến tính cho _f_ ( _X_ ) hầu như luôn là một phép xấp xỉ của thực tế, vì vậy có thêm một nguồn sai số có khả năng giảm thiểu khác mà chúng ta gọi là độ chệch mô hình (_model bias_). Vì vậy, khi chúng ta sử dụng một mô hình tuyến tính, thực tế là chúng ta đang ước lượng phép xấp xỉ tuyến tính tốt nhất cho bề mặt thực. Tuy nhiên, ở đây chúng ta sẽ bỏ qua sự sai lệch này, và tiến hành như thể mô hình tuyến tính là chính xác.

3. Ngay cả khi chúng ta biết _f_ ( _X_ ) — tức là, ngay cả khi chúng ta biết các giá trị thực của _β_ 0 _, β_ 1 _, . . . , βp_ — thì giá trị phản hồi cũng không thể được dự báo một cách hoàn hảo do sai số ngẫu nhiên _ϵ_ trong mô hình (3.20). Trong Chương 2, chúng ta đã gọi đây là _sai số không thể giảm thiểu_ (irreducible error). _Y_ sẽ sai lệch bao nhiêu so với _Y_<sup>ˆ</sup>? Chúng ta sử dụng các _khoảng dự báo_ (prediction intervals) để trả lời câu hỏi này. Khoảng dự báo luôn rộng hơn khoảng tin cậy, bởi vì chúng kết hợp cả sai số trong ước lượng cho _f_ ( _X_ ) (sai số có thể giảm thiểu) và sự không chắc chắn về mức độ mà một điểm riêng lẻ sẽ khác biệt so với mặt phẳng hồi quy quần thể (sai số không thể giảm thiểu).

Chúng ta sử dụng một _khoảng tin cậy_ để định lượng sự không chắc chắn xung quanh mức `sales` _trung bình_ trên một số lượng lớn các thành phố. Ví dụ, cho trước khoản tiền $100 _,_ 000 được chi cho quảng cáo trên `TV` và $20 _,_ 000 được chi cho quảng cáo trên `radio` ở mỗi thành phố, khoảng tin cậy 95 % là [10 _,_ 985 _,_ 11 _,_ 528]. Chúng ta diễn giải điều này có nghĩa là 95 % các khoảng có dạng này sẽ chứa giá trị thực của _f_ ( _X_ ).<sup>9</sup> Mặt khác, một _khoảng dự báo_ có thể được sử dụng để định lượng sự không chắc chắn của dự báo xung quanh mức `sales` của một thành phố _cụ thể_ . 

interval

> 9Nói cách khác, nếu chúng ta thu thập một số lượng lớn các tập dữ liệu giống như tập dữ liệu `Advertising`, và chúng ta xây dựng một khoảng tin cậy cho mức `sales` trung bình trên cơ sở từng tập dữ liệu (cho trước $100 _,_ 000 cho `TV` và $20 _,_ 000 cho quảng cáo trên `radio`), thì 95 % của các khoảng tin cậy này sẽ chứa giá trị thực của mức `sales` trung bình.

3.3 Other Considerations in the Regression Model 83

Cho trước khoản tiền $100 _,_ 000 được chi cho quảng cáo trên `TV` và $20 _,_ 000 được chi cho quảng cáo trên `radio` ở thành phố đó, khoảng dự báo 95 % là [7 _,_ 930 _,_ 14 _,_ 580]. Chúng ta diễn giải điều này có nghĩa là 95 % các khoảng có dạng này sẽ chứa giá trị thực của _Y_ cho thành phố này. Lưu ý rằng cả hai khoảng đều có tâm tại 11 _,_ 256, nhưng khoảng dự báo rộng hơn đáng kể so với khoảng tin cậy, phản ánh sự gia tăng độ không chắc chắn đối với mức `sales` cho một thành phố nhất định so với mức `sales` trung bình ở nhiều địa điểm.

## 3.3 Các cân nhắc khác trong Mô hình hồi quy

### _3.3.1 Các biến dự báo định tính (Qualitative Predictors)_

Trong cuộc thảo luận của chúng ta từ trước đến nay, chúng ta đã giả định rằng tất cả các biến trong mô hình hồi quy tuyến tính của chúng ta đều là _định lượng_ (quantitative). Nhưng trong thực tế, điều này không nhất thiết phải như vậy; thông thường, một số biến dự báo là _định tính_ (qualitative).

Ví dụ, tập dữ liệu `Credit` hiển thị trong Hình 3.6 ghi lại các biến số về một số người sử dụng thẻ tín dụng. Biến phản hồi là `balance` (dư nợ thẻ tín dụng trung bình đối với mỗi cá nhân) và có một số biến dự báo định lượng: `age` , `cards` (số lượng thẻ tín dụng), `education` (số năm học), `income` (tính bằng hàng nghìn đô la), `limit` (hạn mức tín dụng) và `rating` (điểm tín dụng). Mỗi ô của Hình 3.6 là một biểu đồ phân tán (scatterplot) cho một cặp biến số mà định danh của chúng được đưa ra bởi các nhãn hàng và cột tương ứng. Ví dụ, biểu đồ phân tán trực tiếp ở bên phải chữ "Balance" mô tả `balance` so với `age` , trong khi đồ thị trực tiếp bên phải chữ "Age" tương ứng với `age` so với `cards` . Ngoài các biến định lượng này, chúng ta còn có bốn biến định tính: `own` (sở hữu nhà), `student` (tình trạng sinh viên), `status` (tình trạng hôn nhân), và `region` (Đông - East, Tây - West hoặc Nam - South).

#### Các biến dự báo chỉ có hai mức (Levels)

Giả sử rằng chúng ta muốn điều tra sự khác biệt về dư nợ thẻ tín dụng (credit card balance) giữa những người sở hữu nhà và những người không sở hữu, tạm thời bỏ qua các biến số khác. Nếu một biến dự báo định tính (còn được gọi là một _yếu tố_ - factor) chỉ có hai _mức_ (levels), hoặc các giá trị có thể có, thì việc đưa nó vào một mô hình hồi quy rất đơn giản. Chúng ta chỉ cần tạo một biến chỉ báo hoặc _biến giả_ (dummy variable) có thể nhận hai giá trị số.<sup>10</sup> Ví dụ, dựa trên biến `own` , chúng ta có thể tạo ra một biến mới có dạng

variable

![](images/chapter_3.pdf-0025-09.png)

> 10Trong cộng đồng học máy (machine learning), việc tạo ra các biến giả để xử lý các biến dự báo định tính được gọi là mã hóa one-hot ("one-hot encoding").

84 3. Linear Regression

![](images/chapter_3.pdf-0026-01.png)

**HÌNH 3.6.** _Tập dữ liệu_ `Credit` _chứa thông tin về_ `balance` _,_ `age` _,_ `cards` _,_ `education` _,_ `income` _,_ `limit` _, và_ `rating` _đối với một số khách hàng tiềm năng._

và sử dụng biến này làm biến dự báo trong phương trình hồi quy. Điều này dẫn đến mô hình

![](images/chapter_3.pdf-0026-04.png)

Bây giờ _β_ 0 có thể được diễn giải là dư nợ thẻ tín dụng trung bình của những người không sở hữu nhà, _β_ 0 + _β_ 1 là dư nợ thẻ tín dụng trung bình của những người sở hữu nhà của họ, và _β_ 1 là chênh lệch trung bình về dư nợ thẻ tín dụng giữa người sở hữu và người không sở hữu nhà. Bảng 3.7 hiển thị các ước lượng hệ số và các thông tin khác liên quan đến mô hình (3.27). Dư nợ thẻ tín dụng trung bình của những người không sở hữu nhà được ước lượng là $509 _._ 80, trong khi những người sở hữu nhà được ước lượng có thêm khoản nợ $19 _._ 73, cho tổng cộng là $509 _._ 80 + $19 _._ 73 = $529 _._ 53. Tuy nhiên, chúng ta

3.3 Other Considerations in the Regression Model 85

||Hệ số (Coefficient)|Sai số chuẩn (Std. error)|Thống kê _t_ (_t_-statistic)|_p_-value|
|---|---|---|---|---|
|`Intercept`|509.80|33.13|15.389|_<_0_._0001|
|`own[Yes]`|19.73|46.05|0.429|0.6690|

**BẢNG 3.7.** _Các ước lượng hệ số bình phương tối thiểu liên quan đến hồi quy của_ `balance` _theo_ `own` _trong tập dữ liệu_ `Credit` _. Mô hình tuyến tính được cho trong (3.27). Nghĩa là, quyền sở hữu được mã hóa như một biến giả, như trong (3.26)._

nhận thấy rằng _p_ -value của biến giả là rất cao. Điều này chỉ ra rằng không có bằng chứng thống kê nào về sự khác biệt đối với dư nợ thẻ tín dụng trung bình dựa trên việc sở hữu nhà ở.

Quyết định mã hóa những người sở hữu nhà là 1 và không sở hữu nhà là 0 trong (3.27) là tùy ý, và không ảnh hưởng đến sự phù hợp (fit) của hồi quy, nhưng nó làm thay đổi cách diễn giải của các hệ số. Nếu chúng ta mã hóa những người không sở hữu nhà là 1 và những người sở hữu nhà là 0, thì các ước lượng cho _β_ 0 và _β_ 1 sẽ tương ứng là 529 _._ 53 và _−_ 19 _._ 73, lại một lần nữa dẫn đến một dự báo về dư nợ thẻ tín dụng là $529 _._ 53 _−_ $19 _._ 73 = $509 _._ 80 cho những người không sở hữu nhà và một dự báo là $529 _._ 53 cho những người sở hữu nhà. Mặt khác, thay vì sử dụng sơ đồ mã hóa 0 _/_ 1, chúng ta có thể tạo ra một biến giả

![](images/chapter_3.pdf-0027-05.png)

và sử dụng biến này trong phương trình hồi quy. Điều này dẫn đến mô hình

![](images/chapter_3.pdf-0027-07.png)

Bây giờ _β_ 0 có thể được diễn giải là dư nợ thẻ tín dụng trung bình tổng thể (bỏ qua ảnh hưởng của việc sở hữu nhà) và _β_ 1 là lượng mà những người sở hữu nhà và không sở hữu nhà có dư nợ thẻ tín dụng cao hơn và thấp hơn so với mức trung bình tương ứng.<sup>11</sup> Trong ví dụ này, ước lượng cho _β_ 0 là $519 _._ 665, nằm ngay giữa điểm trung bình của người không sở hữu và người sở hữu là $509 _._ 80 và $529 _._ 53. Ước lượng cho _β_ 1 là $9 _._ 865, bằng một nửa của $19 _._ 73, mức chênh lệch trung bình giữa người sở hữu và người không sở hữu. Cần lưu ý rằng các dự báo cuối cùng đối với dư nợ tín dụng của người sở hữu nhà và người không sở hữu nhà sẽ giống hệt nhau bất kể sơ đồ mã hóa nào được sử dụng. Sự khác biệt duy nhất là ở cách diễn giải các hệ số.

#### Các biến dự báo định tính có nhiều hơn hai mức

Khi một biến dự báo định tính có nhiều hơn hai mức, một biến giả đơn lẻ không thể biểu diễn tất cả các giá trị có thể. Trong tình huống này, chúng ta có thể tạo

> 11Về mặt kỹ thuật, _β_ 0 bằng một nửa tổng số nợ trung bình của những người sở hữu nhà và những người không sở hữu nhà. Do đó, _β_ 0 chỉ bằng chính xác mức trung bình tổng thể nếu hai nhóm này có số lượng thành viên bằng nhau.

86 3. Linear Regression

các biến giả bổ sung. Ví dụ, đối với biến `region` , chúng bản tạo hai biến giả. Biến thứ nhất có thể là

![](images/chapter_3.pdf-0028-02.png)

và biến thứ hai có thể là

![](images/chapter_3.pdf-0028-04.png)

Sau đó, cả hai biến này đều có thể được sử dụng trong phương trình hồi quy, để có được mô hình

![](images/chapter_3.pdf-0028-06.png)

Bây giờ _β_ 0 có thể được diễn giải là dư nợ thẻ tín dụng trung bình đối với các cá nhân từ khu vực Đông (East), _β_ 1 có thể được diễn giải là sự chênh lệch trong số dư trung bình giữa những người đến từ khu vực Nam (South) so với khu vực Đông, và _β_ 2 có thể được diễn giải là chênh lệch trong số dư trung bình giữa những người đến từ khu vực Tây (West) so với khu vực Đông. Sẽ luôn có ít hơn số mức một biến giả. Mức không có biến giả — trong ví dụ này là East — được gọi là _đường cơ sở_ (baseline).

Từ Bảng 3.8, chúng ta thấy rằng `balance` ước lượng cho baseline, East, là $531 _._ 00. Người ta ước lượng rằng những người ở khu vực Nam sẽ có dư nợ ít hơn $18 _._ 69 so với những người ở khu vực Đông, và những người ở khu vực Tây sẽ có dư nợ ít hơn $12 _._ 50 so với những người ở khu vực Đông. Tuy nhiên, các _p_ -value liên quan đến các ước lượng hệ số đối với hai biến giả này là rất lớn, cho thấy không có bằng chứng thống kê về một sự khác biệt thực sự về dư nợ thẻ tín dụng trung bình giữa khu vực Nam và Đông hoặc giữa khu vực Tây và Đông.<sup>12</sup> Một lần nữa, mức được chọn làm danh mục baseline là tùy ý và các dự báo cuối cùng đối với mỗi nhóm sẽ giống hệt nhau bất kể sự lựa chọn này. Tuy nhiên, các hệ số và _p_ -value của chúng phụ thuộc vào sự lựa chọn mã hóa biến giả. Thay vì dựa vào các hệ số riêng lẻ, chúng ta có thể sử dụng kiểm định _F_ ( _F_ -test) để kiểm tra _H_ 0 : _β_ 1 = _β_ 2 = 0; điều này không phụ thuộc vào việc mã hóa. Kiểm định _F_ này có một _p_ -value là 0 _._ 96, chỉ ra rằng chúng ta không thể bác bỏ giả thuyết null rằng không có mối quan hệ nào giữa `balance` và `region` .

Sử dụng phương pháp biến giả này không gặp khó khăn gì khi kết hợp cả biến dự báo định lượng và định tính. Ví dụ, để hồi quy `balance` theo cả biến định lượng như `income` và biến định tính như `student` , chúng ta chỉ cần tạo một biến giả

baseline

> 12Về lý thuyết, vẫn có thể có sự khác biệt giữa khu vực Nam và Tây, mặc dù dữ liệu ở đây không gợi ý bất kỳ sự khác biệt nào.

3.3 Other Considerations in the Regression Model 87

||Hệ số (Coefficient)|Sai số chuẩn (Std. error)|Thống kê _t_ (_t_-statistic)|_p_-value|
|---|---|---|---|---|
|`Intercept`|531.00|46.32|11.464|_<_0_._0001|
|`region[South]`|_−_12.50|56.68|_−_0.221|0.8260|
|`region[West]`|_−_18.69|65.02|_−_0.287|0.7740|

**BẢNG 3.8.** _Các ước lượng hệ số bình phương tối thiểu liên quan đến hồi quy của_ `balance` _theo_ `region` _trong tập dữ liệu_ `Credit` _. Mô hình tuyến tính được cho trong (3.30). Nghĩa là, region được mã hóa thông qua hai biến giả (3.28) và (3.29)._

cho `student` và sau đó khớp một mô hình hồi quy bội sử dụng `income` và biến giả làm biến dự báo cho dư nợ thẻ tín dụng.

Có nhiều cách khác nhau để mã hóa các biến định tính bên cạnh cách tiếp cận biến giả được trình bày ở đây. Tất cả các phương pháp này đều dẫn đến độ khớp mô hình tương đương, nhưng các hệ số khác nhau và có các cách diễn giải khác nhau, và được thiết kế để đo lường những sự _tương phản_ (contrasts) cụ thể. Chủ đề contrast này nằm ngoài phạm vi của cuốn sách.


### _3.3.2 Các Mở Rộng của Mô Hình Tuyến Tính_ 

Mô hình hồi quy tuyến tính tiêu chuẩn (3.19) cung cấp các kết quả dễ diễn giải và hoạt động khá tốt trên nhiều bài toán thực tế. Tuy nhiên, nó đưa ra một số giả định mang tính hạn chế cao thường bị vi phạm trong thực tế. Hai trong số các giả định quan trọng nhất phát biểu rằng mối quan hệ giữa các biến dự báo và biến phản hồi có tính _cộng_ (additive) và _tuyến tính_ (linear). Giả định tính cộng có nghĩa là sự liên kết giữa một biến dự báo _Xj_ và biến phản hồi _Y_ không phụ thuộc vào giá trị của các biến dự báo khác. Giả định tuyến tính phát biểu rằng sự thay đổi của biến phản hồi _Y_ liên quan đến một đơn vị thay đổi của _Xj_ là hằng số, bất kể giá trị của _Xj_ . Trong các chương sau của cuốn sách này, chúng ta sẽ xem xét một số phương pháp phức tạp nới lỏng hai giả định này. Ở đây, chúng ta sẽ xem xét ngắn gọn một số cách tiếp cận cổ điển phổ biến để mở rộng mô hình tuyến tính. 

#### Loại Bỏ Giả Định Tính Cộng 

Trong phân tích trước đây của chúng ta về dữ liệu `Advertising`, chúng ta đã kết luận rằng cả `TV` và `radio` dường như đều có liên quan đến `sales`. Các mô hình tuyến tính là cơ sở cho kết luận này đã giả định rằng tác động lên `sales` của việc tăng thêm một phương tiện quảng cáo là độc lập với số tiền chi cho các phương tiện khác. Ví dụ, mô hình tuyến tính (3.20) phát biểu rằng mức tăng trung bình của `sales` liên quan đến một đơn vị tăng của `TV` luôn luôn là _β_ 1, bất kể số tiền chi cho `radio`. 

Tuy nhiên, mô hình đơn giản này có thể không chính xác. Giả sử rằng việc chi tiền cho quảng cáo trên đài phát thanh thực sự làm tăng hiệu quả của quảng cáo trên TV, do đó hệ số góc cho `TV` sẽ tăng lên khi `radio` tăng. Trong tình huống này, với một ngân sách cố định là $100 _,_ 000, việc dành một nửa cho `radio` và một nửa cho `TV` có thể làm tăng `sales` nhiều hơn so với việc phân bổ toàn bộ số tiền 

88 3. Hồi Quy Tuyến Tính 

cho `TV` hoặc cho `radio`. Trong marketing, điều này được gọi là hiệu ứng _hợp lực_ (synergy), và trong thống kê nó được gọi là hiệu ứng _tương tác_ (interaction). Hình 3.5 gợi ý rằng một hiệu ứng như vậy có thể hiện diện trong dữ liệu quảng cáo. Lưu ý rằng khi mức của `TV` hoặc `radio` đều thấp, thì giá trị `sales` thực sự thấp hơn so với dự đoán của mô hình tuyến tính. Nhưng khi quảng cáo được chia đều cho hai phương tiện, thì mô hình có xu hướng đánh giá thấp `sales`. 

Hãy xem xét mô hình hồi quy tuyến tính tiêu chuẩn với hai biến, 


![](images/chapter_3.pdf-0030-03.png)


Theo mô hình này, một đơn vị tăng của _X_ 1 liên quan đến mức tăng trung bình của _Y_ là _β_ 1 đơn vị. Lưu ý rằng sự hiện diện của _X_ 2 không làm thay đổi nhận định này—nghĩa là, bất kể giá trị của _X_ 2, một đơn vị tăng của _X_ 1 liên quan đến sự tăng _β_ 1 đơn vị của _Y_. Một cách để mở rộng mô hình này là đưa vào một biến dự báo thứ ba, được gọi là _số hạng tương tác_ (interaction term), được xây dựng bằng cách tính tích của _X_ 1 và _X_ 2. Điều này dẫn đến mô hình 


![](images/chapter_3.pdf-0030-05.png)


Làm thế nào mà việc đưa vào số hạng tương tác này lại nới lỏng giả định tính cộng? Lưu ý rằng (3.31) có thể được viết lại thành 


![](images/chapter_3.pdf-0030-07.png)


trong đó _β_<sup>˜</sup> 1 = _β_ 1 + _β_ 3 _X_ 2. Vì _β_<sup>˜</sup> 1 giờ đây là một hàm của _X_ 2, sự liên kết giữa _X_ 1 và _Y_ không còn là hằng số nữa: một sự thay đổi giá trị của _X_ 2 sẽ làm thay đổi sự liên kết giữa _X_ 1 và _Y_ . Một lập luận tương tự cho thấy rằng một sự thay đổi giá trị của _X_ 1 sẽ làm thay đổi sự liên kết giữa _X_ 2 và _Y_ . 

Ví dụ, giả sử rằng chúng ta quan tâm đến việc nghiên cứu năng suất của một nhà máy. Chúng ta muốn dự đoán số lượng `units` được sản xuất dựa trên số lượng `lines` sản xuất và tổng số `workers`. Có vẻ như hiệu quả của việc tăng số lượng dây chuyền sản xuất sẽ phụ thuộc vào số lượng công nhân, vì nếu không có công nhân nào để vận hành các dây chuyền, thì việc tăng số lượng dây chuyền sẽ không làm tăng sản lượng. Điều này gợi ý rằng việc đưa vào một số hạng tương tác giữa `lines` và `workers` trong một mô hình tuyến tính để dự đoán `units` sẽ là phù hợp. Giả sử rằng khi chúng ta khớp mô hình, chúng ta thu được 


![](images/chapter_3.pdf-0030-10.png)


Nói cách khác, việc thêm một dây chuyền sẽ làm tăng số lượng đơn vị được sản xuất lên 3 _._ 4 + 1 _._ 4 _×_ `workers`. Do đó, càng có nhiều `workers`, tác động của `lines` sẽ càng mạnh mẽ. 

3.3 Các Cân Nhắc Khác Trong Mô Hình Hồi Quy 89 

||Coefcient|Std. error|_t_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|6.7502|0.248|27.23|_<_0_._0001|
|`TV`|0.0191|0.002|12.70|_<_0_._0001|
|`radio`|0.0289|0.009|3.24|0.0014|
|`TV`_×_`radio`|0.0011|0.000|20.73|_<_0_._0001|



**BẢNG 3.9.** _Đối với dữ liệu_ `Advertising` _, các ước lượng hệ số bình phương tối thiểu liên quan đến hồi quy của_ `sales` _lên_ `TV` _và_ `radio` _, với một số hạng tương tác, như trong (3.33)._ 

Bây giờ chúng ta trở lại ví dụ `Advertising`. Một mô hình tuyến tính sử dụng `radio`, `TV`, và một tương tác giữa hai biến này để dự đoán `sales` có dạng 


![](images/chapter_3.pdf-0031-04.png)


Chúng ta có thể diễn giải _β_ 3 như là sự gia tăng hiệu quả của quảng cáo TV liên quan đến một đơn vị tăng của quảng cáo radio (hoặc ngược lại). Các hệ số thu được từ việc khớp mô hình (3.33) được cho trong Bảng 3.9. 

Các kết quả trong Bảng 3.9 cho thấy mạnh mẽ rằng mô hình bao gồm số hạng tương tác tốt hơn so với mô hình chỉ chứa các _hiệu ứng chính_ (main effects). Giá trị _p_ cho số hạng tương tác, `TV` _×_ `radio`, là cực kỳ thấp, chỉ ra rằng có bằng chứng mạnh mẽ cho _Ha_ : _β_ 3 = 0. Nói cách khác, rõ ràng là mối quan hệ thực sự không mang tính cộng. Giá trị _R_<sup>2</sup> cho mô hình (3.33) là 96.8 %, so với chỉ 89.7 % đối với mô hình dự đoán `sales` bằng `TV` và `radio` mà không có số hạng tương tác. Điều này có nghĩa là (96 _._ 8 _−_ 89 _._ 7) _/_ (100 _−_ 89 _._ 7) = 69 % sự biến thiên của `sales` còn lại sau khi khớp mô hình cộng đã được giải thích bởi số hạng tương tác. Các ước lượng hệ số trong Bảng 3.9 gợi ý rằng việc tăng quảng cáo TV thêm $1 _,_ 000 liên quan đến việc tăng doanh số lên ( _β_<sup>ˆ</sup> 1 + _β_<sup>ˆ</sup> 3 _×_ `radio` ) _×_ 1 _,_ 000 = 19+1 _._ 1 _×_ `radio` đơn vị. Và việc tăng quảng cáo radio thêm $1 _,_ 000 sẽ liên quan đến việc tăng doanh số lên ( _β_<sup>ˆ</sup> 2 + _β_<sup>ˆ</sup> 3 _×_ `TV` ) _×_ 1 _,_ 000 = 29 + 1 _._ 1 _×_ `TV` đơn vị. 

Trong ví dụ này, các giá trị _p_ liên quan đến `TV`, `radio`, và số hạng tương tác đều có ý nghĩa thống kê (Bảng 3.9), và do đó rõ ràng là cả ba biến đều nên được đưa vào mô hình. Tuy nhiên, đôi khi có trường hợp một số hạng tương tác có giá trị _p_ rất nhỏ, nhưng các hiệu ứng chính (trong trường hợp này là `TV` và `radio`) thì không. _Nguyên lý phân cấp_ (hierarchical principle) phát biểu rằng _nếu chúng ta đưa một tương tác vào một mô hình, chúng ta cũng nên đưa vào các hiệu ứng chính, ngay cả khi các giá trị p liên quan đến các hệ số của chúng không có ý nghĩa._ Nói cách khác, nếu tương tác giữa _X_ 1 và _X_ 2 dường như quan trọng, thì chúng ta nên đưa cả _X_ 1 và _X_ 2 vào mô hình ngay cả khi các ước lượng hệ số của chúng có giá trị _p_ lớn. Lý do cho nguyên lý này là nếu _X_ 1 _× X_ 2 có liên quan đến biến phản hồi, thì việc các hệ số của _X_ 1 hay _X_ 2 có chính xác bằng không hay không chỉ mang lại ít 

90 3. Hồi Quy Tuyến Tính 

sự quan tâm. Ngoài ra _X_ 1 _× X_ 2 thường có tương quan với _X_ 1 và _X_ 2, và do đó việc bỏ chúng ra có xu hướng làm thay đổi ý nghĩa của tương tác. 

Trong ví dụ trước, chúng ta đã xem xét một tương tác giữa `TV` và `radio`, cả hai đều là các biến định lượng. Tuy nhiên, khái niệm tương tác cũng áp dụng tương tự cho các biến định tính, hoặc cho sự kết hợp giữa các biến định lượng và định tính. Thực tế, một tương tác giữa một biến định tính và một biến định lượng có một cách diễn giải đặc biệt thú vị. Hãy xem xét tập dữ liệu `Credit` từ Mục 3.3.1, và giả sử rằng chúng ta muốn dự đoán `balance` sử dụng các biến `income` (định lượng) và `student` (định tính). Khi không có số hạng tương tác, mô hình có dạng 


![](images/chapter_3.pdf-0032-03.png)


Lưu ý rằng điều này tương đương với việc khớp hai đường song song với dữ liệu, một cho sinh viên và một cho người không phải sinh viên. Các đường cho sinh viên và người không phải sinh viên có các tung độ gốc khác nhau, _β_ 0 + _β_ 2 so với _β_ 0, nhưng có cùng hệ số góc, _β_ 1. Điều này được minh họa ở bảng điều khiển bên trái của Hình 3.7. Thực tế là các đường song song có nghĩa là hiệu ứng trung bình lên `balance` của một đơn vị tăng trong `income` không phụ thuộc vào việc cá nhân đó có phải là sinh viên hay không. Điều này đại diện cho một hạn chế có thể rất nghiêm trọng của mô hình, bởi vì trên thực tế một sự thay đổi trong `income` có thể có hiệu ứng rất khác nhau lên số dư thẻ tín dụng của một sinh viên so với một người không phải sinh viên. 

Hạn chế này có thể được giải quyết bằng cách thêm một biến tương tác, được tạo ra bằng cách nhân `income` với biến giả cho `student`. Mô hình của chúng ta bây giờ trở thành 


![](images/chapter_3.pdf-0032-06.png)


Một lần nữa, chúng ta có hai đường hồi quy khác nhau cho sinh viên và những người không phải sinh viên. Nhưng bây giờ các đường hồi quy đó có các tung độ gốc khác nhau, _β_ 0+ _β_ 2 so với _β_ 0, cũng như các hệ số góc khác nhau, _β_ 1+ _β_ 3 so với _β_ 1. Điều này cho phép khả năng là những thay đổi trong thu nhập có thể ảnh hưởng đến số dư thẻ tín dụng của sinh viên và người không phải sinh viên một cách khác nhau. Bảng điều khiển bên phải của Hình 3.7 cho thấy các mối quan hệ được ước lượng giữa `income` và `balance` cho sinh viên 

3.3 Các Cân Nhắc Khác Trong Mô Hình Hồi Quy 91 


![](images/chapter_3.pdf-0033-01.png)


**HÌNH 3.7.** _Đối với dữ liệu_ `Credit` _, các đường bình phương tối thiểu được hiển thị để dự đoán_ `balance` _từ_ `income` _cho sinh viên và người không phải sinh viên._ Trái: _Mô hình (3.34) đã được khớp. Không có tương tác giữa_ `income` _và_ `student` _._ Phải: _Mô hình (3.35) đã được khớp. Có một số hạng tương tác giữa_ `income` _và_ `student` _._ 

và người không phải sinh viên trong mô hình (3.35). Chúng ta lưu ý rằng hệ số góc cho sinh viên thấp hơn hệ số góc cho người không phải sinh viên. Điều này gợi ý rằng sự gia tăng trong thu nhập liên quan đến sự gia tăng nhỏ hơn trong số dư thẻ tín dụng ở nhóm sinh viên so với những người không phải sinh viên. 

#### Các Mối Quan Hệ Phi Tuyến Tính 

Như đã thảo luận trước đây, mô hình hồi quy tuyến tính (3.19) giả định một mối quan hệ tuyến tính giữa biến phản hồi và các biến dự báo. Nhưng trong một số trường hợp, mối quan hệ thực sự giữa biến phản hồi và các biến dự báo có thể là phi tuyến tính. Ở đây, chúng tôi trình bày một cách rất đơn giản để mở rộng trực tiếp mô hình tuyến tính nhằm điều chỉnh các mối quan hệ phi tuyến tính, sử dụng _hồi quy đa thức_ (polynomial regression). Trong các chương sau, chúng tôi sẽ trình bày các phương pháp phức tạp hơn để thực hiện hồi quy phi tuyến trong các bối cảnh tổng quát hơn. 

Hãy xem xét Hình 3.8, trong đó `mpg` (mức tiêu thụ nhiên liệu tính bằng dặm trên gallon) so với `horsepower` được hiển thị cho một số xe trong tập dữ liệu `Auto`. Đường màu cam thể hiện sự khớp của hồi quy tuyến tính. Có một mối quan hệ rõ rệt giữa `mpg` và `horsepower`, nhưng có vẻ rõ ràng là mối quan hệ này thực tế là phi tuyến tính: dữ liệu gợi ý một mối quan hệ dạng cong. Một phương pháp đơn giản để kết hợp các liên kết phi tuyến tính vào một mô hình tuyến tính là đưa vào các phiên bản đã được biến đổi của các biến dự báo. Ví dụ, các điểm trong Hình 3.8 dường như có hình dạng _bậc hai_ (quadratic), gợi ý rằng một mô hình có dạng bậc hai 


![](images/chapter_3.pdf-0033-07.png)


có thể cung cấp một sự khớp tốt hơn. Phương trình 3.36 liên quan đến việc dự đoán `mpg` bằng một hàm phi tuyến của `horsepower`. _Nhưng nó vẫn là một mô hình tuyến tính!_ Tức là, (3.36) đơn giản là một mô hình hồi quy tuyến tính bội với _X_ 1 = `horsepower` 


![](images/chapter_3.pdf-0034-00.png)


**HÌNH 3.8.** _Tập dữ liệu_ `Auto` _._ _Đối với một số xe,_ `mpg` _và_ `horsepower` _được hiển thị. Đường khớp hồi quy tuyến tính được hiển thị màu cam. Đường khớp hồi quy tuyến tính cho mô hình bao gồm_ `horsepower`<sup>2</sup> _được hiển thị dưới dạng đường cong màu xanh lam. Đường khớp hồi quy tuyến tính cho một mô hình bao gồm tất cả các đa thức của_ `horsepower` _lên đến bậc năm được hiển thị màu xanh lá cây._ 

||Coefcient|Std. error|_t_-statistic|_p_-value|
|---|---|---|---|---|
|`Intercept`|56.9001|1.8004|31.6|_<_0_._0001|
|`horsepower`|_−_0.4662|0.0311|_−_15.0|_<_0_._0001|
|`horsepower`<sup>2</sup>|0.0012|0.0001|10.1|_<_0_._0001|



**BẢNG 3.10.** _Đối với tập dữ liệu_ `Auto` _, các ước lượng hệ số bình phương tối thiểu liên quan đến hồi quy của_ `mpg` _lên_ `horsepower` _và_ `horsepower`<sup>2</sup> _._ 

và _X_ 2 = `horsepower`<sup>2</sup> . Do đó chúng ta có thể sử dụng phần mềm hồi quy tuyến tính tiêu chuẩn để ước lượng _β_ 0 _, β_ 1, và _β_ 2 nhằm tạo ra một đường khớp phi tuyến. Đường cong màu xanh lam trong Hình 3.8 hiển thị sự khớp bậc hai kết quả đối với dữ liệu. Sự khớp bậc hai dường như tốt hơn đáng kể so với sự khớp thu được khi chỉ đưa vào số hạng tuyến tính. Giá trị _R_<sup>2</sup> của sự khớp bậc hai là 0 _._ 688, so với 0 _._ 606 của sự khớp tuyến tính, và giá trị _p_ trong Bảng 3.10 đối với số hạng bậc hai là rất có ý nghĩa. 

Nếu việc đưa vào `horsepower`<sup>2</sup> dẫn đến một sự cải thiện lớn như vậy trong mô hình, tại sao không đưa vào `horsepower`<sup>3</sup> , `horsepower`<sup>4</sup> , hoặc thậm chí `horsepower`<sup>5</sup> ? Đường cong màu xanh lá cây trong Hình 3.8 hiển thị sự khớp kết quả từ việc đưa vào tất cả các đa thức lên đến bậc năm trong mô hình (3.36). Sự khớp kết quả dường như lượn sóng không cần thiết—nghĩa là, không rõ việc đưa vào các số hạng bổ sung thực sự đã dẫn đến một sự khớp tốt hơn với dữ liệu. 

3.3 Các Cân Nhắc Khác Trong Mô Hình Hồi Quy 

93 

Cách tiếp cận mà chúng ta vừa mô tả để mở rộng mô hình tuyến tính nhằm điều chỉnh các mối quan hệ phi tuyến tính được gọi là _hồi quy đa thức_ , vì chúng ta đã đưa các hàm đa thức của các biến dự báo vào mô hình hồi quy. Chúng ta sẽ khám phá sâu hơn cách tiếp cận này và các phần mở rộng phi tuyến khác của mô hình tuyến tính trong Chương 7. 

### _3.3.3 Các Vấn Đề Tiềm Ẩn_ 

Khi chúng ta khớp một mô hình hồi quy tuyến tính với một tập dữ liệu cụ thể, nhiều vấn đề có thể xảy ra. Phổ biến nhất trong số này là những vấn đề sau: 

1. _Tính phi tuyến tính của các mối quan hệ biến dự báo-biến phản hồi._ 

2. _Sự tương quan của các số hạng sai số._ 

3. _Phương sai không cố định của các số hạng sai số._ 

4. _Các giá trị ngoại lai._ 

5. _Các điểm có đòn bẩy cao._ 

6. _Đa cộng tuyến._ 

Trong thực tế, việc xác định và vượt qua những vấn đề này là một nghệ thuật cũng nhiều như một môn khoa học. Nhiều trang trong vô số cuốn sách đã được viết về chủ đề này. Vì mô hình hồi quy tuyến tính không phải là trọng tâm chính của chúng ta ở đây, chúng tôi sẽ chỉ cung cấp một bản tóm tắt ngắn gọn về một số điểm chính. 

#### 1. Tính Phi Tuyến Tính của Dữ Liệu 

Mô hình hồi quy tuyến tính giả định rằng có một mối quan hệ đường thẳng giữa các biến dự báo và biến phản hồi. Nếu mối quan hệ thực sự cách xa tính tuyến tính, thì hầu như tất cả các kết luận mà chúng ta rút ra từ sự khớp đều đáng ngờ. Ngoài ra, độ chính xác dự đoán của mô hình có thể bị giảm đáng kể. 

_Các biểu đồ phần dư_ (Residual plots) là một công cụ đồ họa hữu ích để xác định tính phi tuyến. Đối với một mô hình hồi quy tuyến tính đơn, chúng ta có thể vẽ các phần dư, _ei_ = _yi −_ ˆ _yi_, so với biến dự báo _xi_. Trong trường hợp của một mô hình hồi quy bội, do có nhiều biến dự báo, thay vào đó chúng ta vẽ các phần dư so với các giá trị được dự đoán (hoặc được _khớp_) ˆ _yi_. Lý tưởng nhất, biểu đồ phần dư sẽ không hiển thị một khuôn mẫu nào có thể nhận biết được. Sự hiện diện của một khuôn mẫu có thể chỉ ra một vấn đề với khía cạnh nào đó của mô hình tuyến tính. 

Bảng điều khiển bên trái của Hình 3.9 hiển thị một biểu đồ phần dư từ hồi quy tuyến tính của `mpg` lên `horsepower` trên tập dữ liệu `Auto` đã được minh họa trong Hình 3.8. Đường màu đỏ là một đường khớp trơn cho các phần dư, được hiển thị nhằm giúp dễ dàng nhận biết bất kỳ xu hướng nào hơn. Các phần dư thể hiện một hình chữ U rõ rệt, cung cấp một dấu hiệu mạnh mẽ về tính phi tuyến tính trong dữ liệu. Ngược lại, bảng điều khiển bên phải của Hình 3.9 hiển thị biểu đồ phần dư 

94 3. Hồi Quy Tuyến Tính 


![](images/chapter_3.pdf-0036-01.png)


**HÌNH 3.9.** _Biểu đồ phần dư so với các giá trị được dự đoán (hoặc được khớp) cho tập dữ liệu_ `Auto` _._ _Trong mỗi biểu đồ, đường màu đỏ là một đường khớp trơn cho các phần dư, nhằm giúp dễ dàng nhận biết một xu hướng hơn._ Trái: _Một hồi quy tuyến tính của_ `mpg` _lên_ `horsepower` _._ _Một khuôn mẫu mạnh mẽ trong các phần dư chỉ ra tính phi tuyến tính trong dữ liệu._ Phải: _Một hồi quy tuyến tính của_ `mpg` _lên_ `horsepower` _và_ `horsepower`<sup>2</sup> _._ _Có rất ít khuôn mẫu trong các phần dư._ 

kết quả từ mô hình (3.36), có chứa một số hạng bậc hai. Dường như có rất ít khuôn mẫu trong các phần dư, gợi ý rằng số hạng bậc hai cải thiện sự khớp đối với dữ liệu. 

Nếu biểu đồ phần dư chỉ ra rằng có các liên kết phi tuyến tính trong dữ liệu, thì một cách tiếp cận đơn giản là sử dụng các phép biến đổi phi tuyến của các biến dự báo, chẳng hạn như log _X_, _√X_, và _X_<sup>2</sup> , trong mô hình hồi quy. Trong các chương sau của cuốn sách này, chúng tôi sẽ thảo luận về các cách tiếp cận phi tuyến nâng cao khác để giải quyết vấn đề này. 

#### 2. Sự Tương Quan của Các Số Hạng Sai Số 

Một giả định quan trọng của mô hình hồi quy tuyến tính là các số hạng sai số, _ϵ_ 1 _, ϵ_ 2 _, . . . , ϵn_ , không có tương quan với nhau. Điều này có ý nghĩa gì? Ví dụ, nếu các sai số không có tương quan, thì việc _ϵi_ mang giá trị dương cung cấp rất ít hoặc không có thông tin gì về dấu của _ϵi_ +1. Các sai số chuẩn được tính toán cho các hệ số hồi quy ước lượng hoặc các giá trị được khớp dựa trên giả định về các số hạng sai số không tương quan. Nếu trên thực tế có sự tương quan giữa các số hạng sai số, thì các sai số chuẩn ước lượng sẽ có xu hướng đánh giá thấp các sai số chuẩn thực sự. Kết quả là, các khoảng tin cậy và khoảng dự đoán sẽ hẹp hơn so với mức chúng nên có. Ví dụ, một khoảng tin cậy 95 % trong thực tế có thể có xác suất thấp hơn nhiều so với 0 _._ 95 để chứa giá trị thực của tham số. Ngoài ra, các giá trị _p_ liên quan đến mô hình sẽ thấp hơn mức chúng nên có; điều này có thể khiến chúng ta kết luận sai rằng một tham số là có ý nghĩa thống kê. 

3.3 Các Cân Nhắc Khác Trong Mô Hình Hồi Quy 95 

Tóm lại, nếu các số hạng sai số có tương quan, chúng ta có thể có một cảm giác tin cậy không chính đáng vào mô hình của mình. 

Như một ví dụ cực đoan, giả sử chúng ta vô tình nhân đôi dữ liệu của mình, dẫn đến các quan sát và các số hạng sai số giống hệt nhau theo từng cặp. Nếu chúng ta phớt lờ điều này, các tính toán sai số chuẩn của chúng ta sẽ giống như thể chúng ta có một mẫu kích thước 2 _n_, trong khi thực tế chúng ta chỉ có _n_ mẫu. Các tham số ước lượng của chúng ta đối với 2 _n_ mẫu sẽ giống như đối với _n_ mẫu, nhưng các khoảng tin cậy sẽ hẹp hơn đi một hệ số là _√_ 2! 

Tại sao các tương quan giữa các số hạng sai số có thể xảy ra? Những tương quan như vậy thường xảy ra trong bối cảnh dữ liệu _chuỗi thời gian_ (time series), bao gồm các quan sát mà các phép đo được thu thập tại các điểm rời rạc trong thời gian. Trong nhiều trường hợp, các quan sát thu được tại các điểm thời gian liền kề sẽ có sai số tương quan dương. Để xác định xem điều này có đúng đối với một tập dữ liệu cụ thể hay không, chúng ta có thể vẽ các phần dư từ mô hình của mình như là một hàm của thời gian. Nếu các sai số không có tương quan, thì sẽ không có khuôn mẫu nào có thể nhận biết được. Mặt khác, nếu các số hạng sai số có tương quan dương, thì chúng ta có thể thấy hiện tượng _bám đuôi_ (tracking) trong các phần dư—nghĩa là, các phần dư liền kề có thể có các giá trị tương tự nhau. Hình 3.10 cung cấp một minh họa. Trong bảng điều khiển trên cùng, chúng ta thấy các phần dư từ một sự khớp hồi quy tuyến tính với dữ liệu được tạo ra với các sai số không tương quan. Không có bằng chứng nào về một xu hướng liên quan đến thời gian trong các phần dư. Ngược lại, các phần dư ở bảng điều khiển dưới cùng là từ một tập dữ liệu trong đó các sai số liền kề có hệ số tương quan là 0 _._ 9. Bây giờ có một khuôn mẫu rõ rệt trong các phần dư—các phần dư liền kề có xu hướng nhận các giá trị tương tự nhau. Cuối cùng, bảng điều khiển ở giữa minh họa một trường hợp vừa phải hơn, trong đó các phần dư có hệ số tương quan là 0 _._ 5. Vẫn có bằng chứng về hiện tượng bám đuôi, nhưng khuôn mẫu ít rõ ràng hơn. 

Nhiều phương pháp đã được phát triển để tính đến đúng đắn các tương quan trong các số hạng sai số của dữ liệu chuỗi thời gian. Sự tương quan giữa các số hạng sai số cũng có thể xảy ra bên ngoài dữ liệu chuỗi thời gian. Ví dụ, hãy xem xét một nghiên cứu trong đó chiều cao của các cá nhân được dự đoán từ cân nặng của họ. Giả định về các sai số không tương quan có thể bị vi phạm nếu một số cá nhân trong nghiên cứu là thành viên của cùng một gia đình, ăn cùng một chế độ ăn uống, hoặc đã tiếp xúc với cùng các yếu tố môi trường. Nói chung, giả định về các sai số không tương quan là cực kỳ quan trọng đối với hồi quy tuyến tính cũng như đối với các phương pháp thống kê khác, và thiết kế thực nghiệm tốt là cốt yếu để giảm thiểu nguy cơ của các tương quan như vậy. 

#### 3. Phương Sai Không Cố Định Của Các Số Hạng Sai Số 

Một giả định quan trọng khác của mô hình hồi quy tuyến tính là các số hạng sai số có một phương sai không đổi, Var( _ϵi_ ) = _σ_<sup>2</sup> . Các sai số chuẩn, khoảng tin cậy, và kiểm định giả thuyết liên quan đến mô hình tuyến tính dựa vào giả định này. 

Thật không may, thường thì phương sai của các số hạng sai số là không cố định. Ví dụ, phương sai của các số hạng sai số có thể tăng 

96 3. Hồi Quy Tuyến Tính 


![](images/chapter_3.pdf-0038-01.png)


**HÌNH 3.10.** _Biểu đồ các phần dư từ các tập dữ liệu chuỗi thời gian mô phỏng được tạo ra với các mức độ tương quan ρ khác nhau giữa các số hạng sai số cho các điểm thời gian liền kề._ 

cùng với giá trị của biến phản hồi. Người ta có thể nhận biết các phương sai không cố định trong các sai số, hay còn gọi là _phương sai thay đổi_ (heteroscedasticity), từ sự hiện diện của một _hình phễu_ (funnel shape) trong biểu đồ phần dư. Một ví dụ được hiển thị ở bảng điều khiển bên trái của Hình 3.11, trong đó độ lớn của các phần dư có xu hướng tăng theo các giá trị được khớp. Khi đối mặt với vấn đề này, một giải pháp khả thi là biến đổi biến phản hồi _Y_ bằng cách sử dụng một hàm lõm như log _Y_ hoặc _√Y_ . Sự biến đổi như vậy dẫn đến một mức độ co ngót lớn hơn đối với các giá trị phản hồi lớn hơn, dẫn đến việc giảm tính phương sai thay đổi. Bảng điều khiển bên phải của Hình 3.11 hiển thị biểu đồ phần dư sau khi biến đổi biến phản hồi sử dụng log _Y_ . Các phần dư bây giờ dường như có phương sai không đổi, mặc dù có một số bằng chứng về một mối quan hệ phi tuyến tính nhẹ trong dữ liệu. 

Đôi khi chúng ta có một ý tưởng tốt về phương sai của từng biến phản hồi. Ví dụ, biến phản hồi thứ _i_ có thể là trung bình của _ni_ quan sát thô. Nếu mỗi một trong số các quan sát thô này không tương quan với phương sai _σ_<sup>2</sup> , thì trung bình của chúng có phương sai _σi_<sup>2=</sup><sup>_σ_2</sup><sup>_/ni_ . Trong trường hợp này, một giải pháp đơn giản là khớp</sup> mô hình của chúng ta bằng _bình phương tối thiểu có trọng số_ (weighted least squares), với các trọng số tỷ lệ thuận với nghịch đảo 

3.3 Các Cân Nhắc Khác Trong Mô Hình Hồi Quy 97 


![](images/chapter_3.pdf-0039-01.png)


**HÌNH 3.11.** _Các biểu đồ phần dư. Trong mỗi biểu đồ, đường màu đỏ là một đường khớp trơn cho các phần dư, nhằm giúp dễ dàng nhận biết một xu hướng hơn. Các đường màu xanh lam bám theo các phân vị bên ngoài của các phần dư, và nhấn mạnh các khuôn mẫu._ Trái: _Hình phễu chỉ ra phương sai thay đổi._ Phải: _Biến phản hồi đã được biến đổi log, và bây giờ không còn bằng chứng nào về phương sai thay đổi._ 

của các phương sai—tức là _wi_ = _ni_ trong trường hợp này. Hầu hết các phần mềm hồi quy tuyến tính đều cho phép sử dụng trọng số cho các quan sát. 


#### 4. Outliers 

Một _điểm dị biệt_ (outlier) là một điểm mà _yi_ khác xa so với giá trị được dự đoán bởi mô hình. Các điểm dị biệt có thể phát sinh vì nhiều lý do, chẳng hạn như việc ghi chép sai một quan sát trong quá trình thu thập dữ liệu. 

Điểm màu đỏ (quan sát 20) ở hình bên trái của Hình 3.12 minh họa một điểm dị biệt điển hình. Đường nét liền màu đỏ là đường hồi quy bình phương tối thiểu, trong khi đường nét đứt màu xanh lam là đường hồi quy bình phương tối thiểu sau khi loại bỏ điểm dị biệt. Trong trường hợp này, việc loại bỏ điểm dị biệt ít có tác động đến đường bình phương tối thiểu: nó dẫn đến hầu như không có thay đổi về độ dốc, và một sự giảm rất nhỏ ở hệ số chặn. Đối với một điểm dị biệt không có giá trị Biến dự báo (Predictor) bất thường, việc nó ít có tác động đến đường bình phương tối thiểu là điều điển hình. Tuy nhiên, ngay cả khi một điểm dị biệt không có nhiều tác động đến đường bình phương tối thiểu, nó vẫn có thể gây ra các vấn đề khác. Ví dụ, trong ví dụ này, RSE là 1 _._ 09 khi điểm dị biệt được đưa vào hồi quy, nhưng nó chỉ là 0 _._ 77 khi điểm dị biệt bị loại bỏ. Vì RSE được sử dụng để tính toán tất cả các khoảng tin cậy và giá trị _p_ (_p_ -values), một sự gia tăng đáng kể như vậy do một điểm dữ liệu duy nhất gây ra có thể có những hệ lụy đối với việc diễn giải mô hình. Tương tự, việc bao gồm điểm dị biệt làm cho _R_<sup>2</sup> giảm từ 0 _._ 892 xuống 0 _._ 805. 

Các biểu đồ phần dư có thể được sử dụng để xác định các điểm dị biệt. Trong ví dụ này, điểm dị biệt có thể được nhìn thấy rõ ràng trong biểu đồ phần dư được minh họa ở hình giữa của Hình 3.12. Nhưng trong thực tế, có thể rất khó để quyết định xem một phần dư cần lớn đến mức nào trước khi chúng ta coi điểm đó là một điểm dị biệt. 

98 3. Linear Regression 


![](images/chapter_3.pdf-0040-01.png)


**HÌNH 3.12.** Trái: _Đường hồi quy bình phương tối thiểu được hiển thị màu đỏ, và đường hồi quy sau khi loại bỏ điểm dị biệt được hiển thị màu xanh lam._ Giữa: _Biểu đồ phần dư xác định rõ ràng điểm dị biệt._ Phải: _Điểm dị biệt có phần dư student hóa (studentized residual) là_ 6 _; thông thường chúng ta kỳ vọng các giá trị nằm trong khoảng từ −_ 3 _đến_ 3 _._ 


![](images/chapter_3.pdf-0040-03.png)


**HÌNH 3.13.** Trái: _Quan sát 41 là một điểm có đòn bẩy cao, trong khi 20 thì không. Đường màu đỏ là đường khớp cho toàn bộ dữ liệu, và đường màu xanh lam là đường khớp với quan sát 41 bị loại bỏ._ Giữa: _Quan sát màu đỏ không bất thường về giá trị X_ 1 _hay giá trị X_ 2 _của nó, nhưng vẫn nằm ngoài phần lớn dữ liệu, và do đó có đòn bẩy cao._ Phải: _Quan sát_ 41 _có đòn bẩy cao và phần dư cao._ 

Để giải quyết vấn đề này, thay vì vẽ các phần dư, chúng ta có thể vẽ các _phần dư student hóa_ (studentized residuals), được tính bằng cách chia mỗi phần dư _ei_ cho sai số chuẩn ước lượng của nó. Các quan sát có phần dư student hóa lớn hơn 3 về giá trị tuyệt đối có thể là các điểm dị biệt. Ở hình bên phải của Hình 3.12, phần dư student hóa của điểm dị biệt vượt quá 6, trong khi tất cả các quan sát khác đều có phần dư student hóa từ _−_ 2 đến 2. 

Nếu chúng ta tin rằng một điểm dị biệt xảy ra do lỗi trong quá trình thu thập hoặc ghi chép dữ liệu, thì một giải pháp là chỉ cần loại bỏ quan sát đó. Tuy nhiên, cần cẩn thận, vì một điểm dị biệt thay vào đó có thể chỉ ra sự thiếu hụt của mô hình, chẳng hạn như thiếu một Biến dự báo. 

#### 5. High Leverage Points 

Chúng ta vừa thấy rằng các điểm dị biệt là các quan sát mà Biến phản hồi (Response) _yi_ là bất thường xét theo Biến dự báo _xi_ . Ngược lại, các quan sát có _đòn bẩy cao_ (high leverage) 

3.3 Other Considerations in the Regression Model 99 

có một giá trị bất thường đối với _xi_ . Ví dụ, quan sát 41 trong hình bên trái của Hình 3.13 có đòn bẩy cao, ở chỗ giá trị Biến dự báo cho quan sát này lớn so với các quan sát khác. (Lưu ý rằng dữ liệu được hiển thị trong Hình 3.13 giống với dữ liệu được hiển thị trong Hình 3.12, nhưng có thêm một quan sát có đòn bẩy cao duy nhất.) Đường nét liền màu đỏ là đường hồi quy bình phương tối thiểu cho dữ liệu, trong khi đường nét đứt màu xanh lam là đường hồi quy được tạo ra khi quan sát 41 bị loại bỏ. So sánh các hình bên trái của Hình 3.12 và 3.13, chúng ta quan sát thấy rằng việc loại bỏ quan sát có đòn bẩy cao có tác động đáng kể hơn nhiều đến đường bình phương tối thiểu so với việc loại bỏ điểm dị biệt. Trên thực tế, các quan sát có đòn bẩy cao có xu hướng có tác động khá lớn đến đường hồi quy ước lượng. Sẽ là một nguyên nhân gây lo ngại nếu đường bình phương tối thiểu bị ảnh hưởng nặng nề bởi chỉ một vài quan sát, bởi vì bất kỳ vấn đề nào với các điểm này có thể làm vô hiệu toàn bộ mô hình. Vì lý do này, việc xác định các quan sát có đòn bẩy cao là rất quan trọng. 

Trong một hồi quy tuyến tính đơn biến, các quan sát có đòn bẩy cao khá dễ xác định, vì chúng ta có thể chỉ cần tìm kiếm các quan sát mà giá trị Biến dự báo nằm ngoài phạm vi bình thường của các quan sát. Nhưng trong một hồi quy tuyến tính đa biến với nhiều Biến dự báo, có thể có một quan sát nằm hoàn toàn trong phạm vi giá trị của từng Biến dự báo riêng lẻ, nhưng lại bất thường xét trên toàn bộ tập hợp các Biến dự báo. Một ví dụ được hiển thị ở hình giữa của Hình 3.13, cho một tập dữ liệu với hai Biến dự báo, _X_ 1 và _X_ 2. Hầu hết các giá trị Biến dự báo của các quan sát rơi vào hình elip nét đứt màu xanh lam, nhưng quan sát màu đỏ lại nằm ngoài phạm vi này. Nhưng cả giá trị của nó đối với _X_ 1 và giá trị của nó đối với _X_ 2 đều không bất thường. Do đó, nếu chúng ta chỉ kiểm tra _X_ 1 hoặc chỉ _X_ 2, chúng ta sẽ không nhận ra điểm có đòn bẩy cao này. Vấn đề này càng rõ rệt hơn trong các thiết lập hồi quy đa biến với hơn hai Biến dự báo, vì khi đó không có cách nào đơn giản để vẽ tất cả các chiều của dữ liệu cùng một lúc. 

Để định lượng đòn bẩy của một quan sát, chúng chúng ta tính toán _thống kê đòn bẩy_ (leverage statistic). Một giá trị lớn của thống kê này chỉ ra một quan sát có đòn bẩy cao. Đối với một hồi quy tuyến tính đơn biến, 


![](images/chapter_3.pdf-0041-05.png)


Rõ ràng từ phương trình này là _hi_ tăng theo khoảng cách của _xi_ so với ¯ _x_ . Có một sự mở rộng đơn giản của _hi_ cho trường hợp có nhiều Biến dự báo, mặc dù chúng tôi không cung cấp công thức ở đây. Thống kê đòn bẩy _hi_ luôn nằm trong khoảng từ 1 _/n_ đến 1, và đòn bẩy trung bình cho tất cả các quan sát luôn bằng ( _p_ + 1) _/n_ . Vì vậy, nếu một quan sát nhất định có thống kê đòn bẩy vượt quá ( _p_ +1) _/n_ một cách đáng kể, thì chúng ta có thể nghi ngờ rằng điểm tương ứng có đòn bẩy cao. 

Hình bên phải của Hình 3.13 cung cấp một biểu đồ của các phần dư student hóa so với _hi_ cho dữ liệu ở hình bên trái của Hình 3.13. Quan sát 41 nổi bật vì có thống kê đòn bẩy rất cao cũng như phần dư student hóa cao. Nói cách khác, nó vừa là một điểm dị biệt vừa là một quan sát 

100 3. Linear Regression 


![](images/chapter_3.pdf-0042-01.png)


**HÌNH 3.14.** _Các biểu đồ phân tán của các quan sát từ tập dữ liệu_ `Credit` _._ Trái: _Một biểu đồ của_ `age` _so với_ `limit` _._ _Hai biến này không đa cộng tuyến._ Phải: _Một biểu đồ của_ `rating` _so với_ `limit` _._ _Có hiện tượng đa cộng tuyến cao._ 

có đòn bẩy cao. Đây là một sự kết hợp đặc biệt nguy hiểm! Biểu đồ này cũng tiết lộ lý do tại sao quan sát 20 lại có tương đối ít ảnh hưởng đến đường bình phương tối thiểu trong Hình 3.12: nó có đòn bẩy thấp. 

#### 6. Collinearity 

_Đa cộng tuyến_ (Collinearity) đề cập đến tình huống trong đó hai hoặc nhiều Biến dự báo có liên quan chặt chẽ với nhau. Khái niệm đa cộng tuyến được minh họa trong Hình 3.14 sử dụng tập dữ liệu `Credit`. Trong hình bên trái của Hình 3.14, hai Biến dự báo `limit` và `age` dường như không có mối quan hệ rõ ràng nào. Ngược lại, trong hình bên phải của Hình 3.14, các Biến dự báo `limit` và `rating` có tương quan rất cao với nhau, và chúng ta nói rằng chúng có hiện tượng _đa cộng tuyến_. Sự hiện diện của hiện tượng đa cộng tuyến có thể gây ra các vấn đề trong ngữ cảnh hồi quy, vì có thể khó tách biệt các tác động riêng lẻ của các biến đa cộng tuyến lên Biến phản hồi. Nói cách khác, vì `limit` và `rating` có xu hướng cùng tăng hoặc cùng giảm, có thể khó để xác định cách mà mỗi biến riêng biệt liên kết với Biến phản hồi, `balance`. 

Hình 3.15 minh họa một số khó khăn có thể phát sinh do hiện tượng đa cộng tuyến. Hình bên trái của Hình 3.15 là một biểu đồ đường viền (contour plot) của RSS (3.22) liên kết với các ước lượng hệ số khả thi khác nhau cho hồi quy của `balance` theo `limit` và `age`. Mỗi hình elip biểu diễn một tập hợp các hệ số tương ứng với cùng một RSS, với các hình elip gần tâm nhất nhận các giá trị RSS thấp nhất. Các dấu chấm màu đen và các đường nét đứt liên quan biểu diễn các ước lượng hệ số dẫn đến RSS nhỏ nhất có thể — nói cách khác, đây là các ước lượng bình phương tối thiểu. Các trục của `limit` và `age` đã được điều chỉnh tỷ lệ để biểu đồ bao gồm các ước lượng hệ số khả thi nằm trong khoảng lên đến bốn sai số chuẩn ở hai bên của các ước lượng bình phương tối thiểu. Do đó, biểu đồ bao gồm tất cả các giá trị hợp lý cho các 

3.3 Other Considerations in the Regression Model 101 


![](images/chapter_3.pdf-0043-01.png)


**HÌNH 3.15.** _Biểu đồ đường viền cho các giá trị RSS dưới dạng một hàm số của các tham số β cho các hồi quy khác nhau liên quan đến tập dữ liệu_ `Credit` _. Trong mỗi biểu đồ, các dấu chấm màu đen biểu diễn các giá trị hệ số tương ứng với RSS nhỏ nhất._ Trái: _Một biểu đồ đường viền của RSS cho hồi quy của_ `balance` _theo_ `age` _và_ `limit` _. Giá trị nhỏ nhất được xác định rõ ràng._ Phải: _Một biểu đồ đường viền của RSS cho hồi quy của_ `balance` _theo_ `rating` _và_ `limit` _. Do hiện tượng đa cộng tuyến, có nhiều cặp_ ( _β_ Limit _, β_ Rating) _với một giá trị RSS tương tự._ 

hệ số. Ví dụ, chúng ta thấy rằng hệ số `limit` thực sự gần như chắc chắn nằm đâu đó giữa 0 _._ 15 và 0 _._ 20. 

Ngược lại, hình bên phải của Hình 3.15 hiển thị các biểu đồ đường viền của RSS liên kết với các ước lượng hệ số khả thi cho hồi quy của `balance` theo `limit` và `rating`, mà chúng ta biết là có tính đa cộng tuyến cao. Bây giờ các đường viền chạy dọc theo một thung lũng hẹp; có một phạm vi rộng các giá trị cho các ước lượng hệ số dẫn đến các giá trị bằng nhau cho RSS. Do đó, một thay đổi nhỏ trong dữ liệu có thể làm cho cặp giá trị hệ số mang lại RSS nhỏ nhất — nghĩa là, các ước lượng bình phương tối thiểu — di chuyển đến bất kỳ đâu dọc theo thung lũng này. Điều này dẫn đến rất nhiều sự không chắc chắn trong các ước lượng hệ số. Lưu ý rằng thang đo cho hệ số `limit` bây giờ chạy từ khoảng _−_ 0 _._ 2 đến 0 _._ 2; đây là mức tăng gấp tám lần so với phạm vi hợp lý của hệ số `limit` trong hồi quy với `age`. Thú vị là, mặc dù các hệ số `limit` và `rating` bây giờ có nhiều sự không chắc chắn cá nhân hơn, chúng gần như chắc chắn sẽ nằm đâu đó trong thung lũng đường viền này. Ví dụ, chúng ta sẽ không kỳ vọng giá trị thực của các hệ số `limit` và `rating` lần lượt là _−_ 0 _._ 1 và 1, mặc dù một giá trị như vậy là hợp lý cho từng hệ số một cách riêng lẻ. 

Vì hiện tượng đa cộng tuyến làm giảm độ chính xác của các ước lượng của các hệ số hồi quy, nó làm cho sai số chuẩn của _β_<sup>ˆ</sup> _j_ tăng lên. Nhớ lại rằng thống kê _t_ cho mỗi Biến dự báo được tính bằng cách chia _β_<sup>ˆ</sup> _j_ cho sai số chuẩn của nó. Do đó, hiện tượng đa cộng tuyến dẫn đến sự suy giảm của thống kê _t_. Kết quả là, khi có hiện tượng đa cộng tuyến, chúng ta có thể không bác bỏ được _H_ 0 : _βj_ = 0. Điều này 

102 3. Linear Regression 

|||Hệ số (Coefficient)|Sai số chuẩn (Std. error)|Thống kê _t_ (_t_-statistic)|Giá trị _p_ (_p_-value)|
|---|---|---|---|---|---|
||`Intercept`|_−_173.411|43.828|_−_3.957|_<_0_._0001|
|Mô hình 1 (Model 1)|`age`|_−_2.292|0.672|_−_3.407|0_._0007|
||`limit`|0.173|0.005|34.496|_<_0_._0001|
||`Intercept`|_−_377.537|45.254|_−_8.343|_<_0_._0001|
|Mô hình 2 (Model 2)|`rating`|2.202|0.952|2.312|0.0213|
||`limit`|0.025|0.064|0.384|0.7012|



**BẢNG 3.11.** _Kết quả của hai mô hình hồi quy đa biến liên quan đến tập dữ liệu_ `Credit` _được hiển thị. Mô hình 1 là một hồi quy của_ `balance` _theo_ `age` _và_ `limit` _, và Mô hình 2 là một hồi quy của_ `balance` _theo_ `rating` _và_ `limit` _. Sai số chuẩn của β_ ˆlimit _tăng gấp 12 lần trong hồi quy thứ hai, do hiện tượng đa cộng tuyến._ 

có nghĩa là _lực_ (power) của kiểm định giả thuyết — xác suất phát hiện chính xác một hệ số _khác không_ — bị giảm đi bởi hiện tượng đa cộng tuyến. 

Bảng 3.11 so sánh các ước lượng hệ số thu được từ hai mô hình hồi quy đa biến riêng biệt. Mô hình đầu tiên là một hồi quy của `balance` theo `age` và `limit`, và mô hình thứ hai là một hồi quy của `balance` theo `rating` và `limit`. Trong hồi quy đầu tiên, cả `age` và `limit` đều có ý nghĩa thống kê rất cao với các giá trị _p_ rất nhỏ. Trong mô hình thứ hai, hiện tượng đa cộng tuyến giữa `limit` và `rating` đã làm cho sai số chuẩn cho ước lượng hệ số `limit` tăng lên với hệ số 12 và giá trị _p_ tăng lên 0 _._ 701. Nói cách khác, tầm quan trọng của biến `limit` đã bị che khuất do sự hiện diện của hiện tượng đa cộng tuyến. Để tránh một tình huống như vậy, việc xác định và giải quyết các vấn đề đa cộng tuyến tiềm ẩn trong khi khớp mô hình là điều đáng mong muốn. 

Một cách đơn giản để phát hiện hiện tượng đa cộng tuyến là nhìn vào ma trận tương quan của các Biến dự báo. Một phần tử của ma trận này lớn về giá trị tuyệt đối chỉ ra một cặp biến có tương quan cao, và do đó có vấn đề đa cộng tuyến trong dữ liệu. Thật không may, không phải tất cả các vấn đề đa cộng tuyến đều có thể được phát hiện bằng cách kiểm tra ma trận tương quan: hiện tượng đa cộng tuyến có thể tồn tại giữa ba hoặc nhiều biến ngay cả khi không có cặp biến nào có tương quan đặc biệt cao. Chúng ta gọi tình huống này là _đa cộng tuyến nhiều biến_ (multicollinearity). 
Thay vì kiểm tra ma trận tương quan, một cách tốt hơn để đánh giá hiện tượng đa cộng tuyến nhiều biến là tính toán _hệ số phóng đại phương sai_ (variance inflation factor - VIF). VIF là tỷ lệ giữa phương sai của _β_<sup>ˆ</sup> _j_ khi khớp mô hình đầy đủ chia cho phương sai của _β_<sup>ˆ</sup> _j_ nếu khớp trên chính nó. Giá trị nhỏ nhất có thể có cho VIF là 1, chỉ ra sự vắng mặt hoàn toàn của hiện tượng đa cộng tuyến. Thông thường trong thực tế có một lượng nhỏ hiện tượng đa cộng tuyến giữa các Biến dự báo. Theo quy tắc ngón tay cái, một giá trị VIF vượt quá 5 hoặc 10 cho thấy một lượng đa cộng tuyến có vấn đề. VIF cho mỗi biến có thể được tính bằng công thức 


![](images/chapter_3.pdf-0044-07.png)


3.4 The Marketing Plan 103 

trong đó _RX_<sup>2</sup> _j |X−j_ <sup>là</sup> <sup>_R_2 từ một mô hình hồi quy của</sup> <sup>_Xj_ lên tất cả các Biến dự báo khác.</sup> Nếu _RX_<sup>2</sup> _j |X−j_ <sup>gần với 1, thì hiện tượng đa cộng tuyến đang hiện diện, và do đó</sup> VIF sẽ lớn. 

Trong dữ liệu `Credit`, một hồi quy của `balance` theo `age`, `rating`, và `limit` chỉ ra rằng các Biến dự báo có các giá trị VIF là 1.01, 160.67, và 160.59. Đúng như chúng ta đã nghi ngờ, có một mức độ đa cộng tuyến đáng kể trong dữ liệu! 

Khi đối mặt với vấn đề đa cộng tuyến, có hai giải pháp đơn giản. Giải pháp đầu tiên là loại bỏ một trong những biến có vấn đề khỏi hồi quy. Điều này thường có thể được thực hiện mà không ảnh hưởng nhiều đến mức độ khớp của hồi quy, vì sự hiện diện của hiện tượng đa cộng tuyến ngụ ý rằng thông tin mà biến này cung cấp về Biến phản hồi là dư thừa khi có sự hiện diện của các biến khác. Ví dụ, nếu chúng ta hồi quy `balance` theo `age` và `limit`, mà không có Biến dự báo `rating`, thì các giá trị VIF thu được gần với giá trị tối thiểu có thể là 1, và _R_<sup>2</sup> giảm từ 0 _._ 754 xuống 0 _._ 75. Do đó, việc loại bỏ `rating` khỏi tập hợp các Biến dự báo đã giải quyết hiệu quả vấn đề đa cộng tuyến mà không ảnh hưởng đến mức độ khớp. Giải pháp thứ hai là kết hợp các biến đa cộng tuyến lại với nhau thành một Biến dự báo duy nhất. Ví dụ, chúng ta có thể lấy trung bình các phiên bản được chuẩn hóa của `limit` và `rating` để tạo ra một biến mới đo lường _mức độ tín nhiệm_ (credit worthiness). 

## 3.4 The Marketing Plan 

Bây giờ chúng ta sẽ nhanh chóng quay lại với bảy câu hỏi về dữ liệu `Advertising` mà chúng ta đã đặt ra để trả lời ở phần đầu của chương này. 

1. _Có mối quan hệ nào giữa doanh số bán hàng và ngân sách quảng cáo không?_ Câu hỏi này có thể được trả lời bằng cách khớp một mô hình hồi quy đa biến của `sales` theo `TV`, `radio`, và `newspaper`, như trong (3.20), và kiểm định giả thuyết _H_ 0 : _β_ `TV` = _β_ `radio` = _β_ `newspaper` = 0. Trong Phần 3.2.2, chúng ta đã chỉ ra rằng thống kê _F_ có thể được sử dụng để quyết định xem liệu chúng ta có nên bác bỏ giả thuyết không này hay không. Trong trường hợp này, giá trị _p_ tương ứng với thống kê _F_ trong Bảng 3.6 rất thấp, cho thấy bằng chứng rõ ràng về mối quan hệ giữa quảng cáo và doanh số bán hàng. 

2. _Mối quan hệ đó mạnh đến mức nào?_ Chúng ta đã thảo luận về hai thước đo độ chính xác của mô hình trong Phần 3.1.3. Đầu tiên, RSE ước lượng độ lệch chuẩn của Biến phản hồi so với đường hồi quy của tổng thể. Đối với dữ liệu `Advertising`, RSE là 1 _._ 69 đơn vị trong khi giá trị trung bình cho Biến phản hồi là 14 _._ 022, cho thấy phần trăm sai số là khoảng 12 %. Thứ hai, thống kê _R_<sup>2</sup> ghi nhận phần trăm của Phương sai (Variance) trong Biến phản hồi được giải thích bởi các Biến dự báo. Các Biến dự báo giải thích gần 90 % của Phương sai trong `sales`. Các thống kê RSE và _R_<sup>2</sup> được hiển thị trong Bảng 3.6. 

104 3. Linear Regression 

3. _Các phương tiện truyền thông nào có liên quan đến doanh số bán hàng?_ Để trả lời câu hỏi này, chúng ta có thể kiểm tra các giá trị _p_ liên kết với thống kê _t_ của mỗi Biến dự báo (Phần 3.1.2). Trong hồi quy tuyến tính đa biến được hiển thị ở Bảng 3.4, các giá trị _p_ cho `TV` và `radio` là thấp, nhưng giá trị _p_ cho `newspaper` thì không. Điều này gợi ý rằng chỉ `TV` và `radio` có liên quan đến `sales`. Trong Chương 6, chúng ta sẽ khám phá câu hỏi này chi tiết hơn. 

4. _Mức độ liên kết giữa mỗi phương tiện và doanh số lớn như thế nào?_ Chúng ta đã thấy trong Phần 3.1.2 rằng sai số chuẩn của _β_<sup>ˆ</sup> _j_ có thể được sử dụng để xây dựng các khoảng tin cậy cho _βj_ . Đối với dữ liệu `Advertising`, chúng ta có thể sử dụng các kết quả trong Bảng 3.4 để tính các khoảng tin cậy 95 % cho các hệ số trong một mô hình hồi quy đa biến sử dụng tất cả ba ngân sách phương tiện truyền thông làm các Biến dự báo. Các khoảng tin cậy như sau: (0 _._ 043 _,_ 0 _._ 049) cho `TV`, (0 _._ 172 _,_ 0 _._ 206) cho `radio`, và ( _−_ 0 _._ 013 _,_ 0 _._ 011) cho `newspaper`. Các khoảng tin cậy cho `TV` và `radio` là hẹp và cách xa không, cung cấp bằng chứng rằng các phương tiện này có liên quan đến `sales`. Nhưng khoảng tin cậy cho `newspaper` bao gồm cả số không, cho thấy biến này không có ý nghĩa thống kê khi xét với các giá trị của `TV` và `radio`. 

   - Chúng ta đã thấy trong Phần 3.3.3 rằng hiện tượng đa cộng tuyến có thể dẫn đến các sai số chuẩn rất rộng. Liệu đa cộng tuyến có thể là lý do khiến khoảng tin cậy liên kết với `newspaper` lại rộng như vậy không? Các điểm số VIF là 1 _._ 005, 1 _._ 145, và 1 _._ 145 lần lượt cho `TV`, `radio`, và `newspaper`, cho thấy không có bằng chứng về đa cộng tuyến. 

Để đánh giá mức độ liên kết của từng phương tiện truyền thông một cách riêng lẻ lên doanh số, chúng ta có thể thực hiện ba mô hình hồi quy tuyến tính đơn biến riêng biệt. Kết quả được hiển thị trong các Bảng 3.1 và 3.3. Có bằng chứng về sự liên kết cực kỳ mạnh mẽ giữa `TV` và `sales` cũng như giữa `radio` và `sales`. Có bằng chứng về sự liên kết nhẹ giữa `newspaper` và `sales`, khi các giá trị của `TV` và `radio` bị bỏ qua. 

5. _Chúng ta có thể dự đoán doanh số bán hàng trong tương lai chính xác đến mức nào?_ Biến phản hồi có thể được dự đoán bằng cách sử dụng (3.21). Độ chính xác liên kết với ước lượng này phụ thuộc vào việc liệu chúng ta muốn dự đoán một Biến phản hồi cá nhân, _Y_ = _f_ ( _X_ ) + _ϵ_ , hay Biến phản hồi trung bình, _f_ ( _X_ ) (Phần 3.2.2). Nếu là trường hợp đầu, chúng ta sử dụng một khoảng dự đoán (prediction interval), và nếu là trường hợp sau, chúng ta sử dụng một khoảng tin cậy. Các khoảng dự đoán sẽ luôn rộng hơn các khoảng tin cậy bởi vì chúng tính đến sự không chắc chắn liên kết với _ϵ_ , sai số không thể giảm thiểu. 

6. _Mối quan hệ này có tuyến tính không?_ 

   - Trong Phần 3.3.3, chúng ta đã thấy rằng các biểu đồ phần dư có thể được sử dụng để xác định tính phi tuyến (non-linearity). Nếu các mối quan hệ là tuyến tính, thì các biểu đồ phần dư không nên hiển thị bất kỳ mô hình nào. Trong trường hợp của dữ liệu `Advertising`, 

3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors 105 

chúng ta quan sát thấy một hiệu ứng phi tuyến tính trong Hình 3.5, mặc dù hiệu ứng này cũng có thể được quan sát thấy trong một biểu đồ phần dư. Trong Phần 3.3.2, chúng ta đã thảo luận về việc bao gồm các phép biến đổi của các Biến dự báo trong mô hình hồi quy tuyến tính để điều chỉnh cho các mối quan hệ phi tuyến. 

7. _Có tính cộng hưởng nào giữa các phương tiện quảng cáo không?_ Mô hình hồi quy tuyến tính chuẩn giả định một mối quan hệ cộng gộp giữa các Biến dự báo và Biến phản hồi. Một mô hình cộng gộp dễ diễn giải bởi vì sự liên kết giữa mỗi Biến dự báo và Biến phản hồi không liên quan đến các giá trị của các Biến dự báo khác. Tuy nhiên, giả định cộng gộp có thể không thực tế đối với các tập dữ liệu nhất định. Trong Phần 3.3.2, chúng ta đã chỉ ra cách bao gồm một thành phần tương tác trong mô hình hồi quy để điều chỉnh cho các mối quan hệ phi cộng gộp. Một giá trị _p_ nhỏ liên kết với thành phần tương tác chỉ ra sự hiện diện của các mối quan hệ như vậy. Hình 3.5 đã gợi ý rằng dữ liệu `Advertising` có thể không có tính cộng gộp. Việc bao gồm một thành phần tương tác trong mô hình dẫn đến sự gia tăng đáng kể của _R_<sup>2</sup> , từ khoảng 90 % lên gần 97 %. 

## 3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors 

Như đã thảo luận trong Chương 2, hồi quy tuyến tính là một ví dụ về một phương pháp _tham số_ (parametric approach) vì nó giả định một dạng hàm số tuyến tính cho _f_ ( _X_ ). Các phương pháp tham số có một số lợi thế. Chúng thường dễ khớp, bởi vì người ta chỉ cần ước lượng một số lượng nhỏ các hệ số. Trong trường hợp hồi quy tuyến tính, các hệ số có những cách diễn giải đơn giản, và các kiểm định ý nghĩa thống kê có thể được thực hiện một cách dễ dàng. Nhưng các phương pháp tham số có một nhược điểm: theo cấu trúc, chúng đưa ra những giả định mạnh mẽ về dạng của _f_ ( _X_ ). Nếu dạng hàm số được chỉ định khác xa với thực tế, và độ chính xác dự đoán là mục tiêu của chúng ta, thì phương pháp tham số sẽ có hiệu suất kém. Ví dụ, nếu chúng ta giả định một mối quan hệ tuyến tính giữa _X_ và _Y_ nhưng mối quan hệ thực sự khác xa so với tuyến tính, thì mô hình kết quả sẽ cung cấp một mức độ khớp kém đối với dữ liệu, và mọi kết luận rút ra từ nó sẽ bị nghi ngờ. 

Ngược lại, các phương pháp _phi tham số_ (non-parametric methods) không giả định một cách rõ ràng một dạng tham số cho _f_ ( _X_ ), và qua đó cung cấp một cách tiếp cận thay thế và linh hoạt hơn để thực hiện hồi quy. Chúng ta sẽ thảo luận về nhiều phương pháp phi tham số khác nhau trong cuốn sách này. Ở đây chúng ta xem xét một trong những phương pháp phi tham số đơn giản nhất và được biết đến nhiều nhất, _hồi quy K láng giềng gần nhất_ (KNN regression). Phương pháp hồi quy KNN liên quan chặt chẽ đến bộ phân loại KNN đã được thảo luận ở Chương 2. Cho một giá trị của _K_ và một điểm dự đoán _x_ 0, đầu tiên hồi quy KNN xác định _K_ quan sát huấn luyện gần nhất với _x_ 0, được biểu diễn bởi _N_ 0. Sau đó nó ước lượng _f_ ( _x_ 0) bằng cách sử dụng trung bình của tất cả 

106 3. Linear Regression 


![](images/chapter_3.pdf-0048-01.png)


**HÌNH 3.16.** _Các biểu đồ của f_<sup>ˆ</sup> ( _X_ ) _sử dụng hồi quy KNN trên một tập dữ liệu hai chiều với_ 64 _quan sát (các chấm màu cam)._ Trái: _K_ = 1 _dẫn đến một đường khớp có dạng hàm bậc thang thô ráp._ Phải: _K_ = 9 _tạo ra một đường khớp mượt mà hơn nhiều._ 

các Biến phản hồi huấn luyện trong _N_ 0. Nói cách khác, 


![](images/chapter_3.pdf-0048-04.png)


Hình 3.16 minh họa hai mô hình khớp KNN trên một tập dữ liệu với _p_ = 2 Biến dự báo. Đường khớp với _K_ = 1 được hiển thị ở hình bên trái, trong khi hình bên phải tương ứng với _K_ = 9. Chúng ta thấy rằng khi _K_ = 1, đường khớp KNN nội suy hoàn hảo các quan sát huấn luyện, và do đó có dạng của một hàm bậc thang. Khi _K_ = 9, đường khớp KNN vẫn là một hàm bậc thang, nhưng việc lấy trung bình trên chín quan sát dẫn đến các khu vực dự đoán không đổi nhỏ hơn nhiều, và do đó một đường khớp mượt mà hơn. Nhìn chung, giá trị tối ưu cho _K_ sẽ phụ thuộc vào _sự cân bằng giữa Độ chệch-Phương sai_ (bias-variance tradeoff), thứ mà chúng ta đã giới thiệu trong Chương 2. Một giá trị nhỏ cho _K_ cung cấp đường khớp linh hoạt nhất, sẽ có Độ chệch (Bias) thấp nhưng Phương sai cao. Phương sai này là do thực tế là dự đoán trong một khu vực nhất định phụ thuộc hoàn toàn vào chỉ một quan sát. Ngược lại, các giá trị lớn hơn của _K_ cung cấp một đường khớp mượt mà hơn và ít biến động hơn; dự đoán trong một khu vực là trung bình của một số điểm, và vì vậy việc thay đổi một quan sát có tác động nhỏ hơn. Tuy nhiên, việc làm mượt có thể gây ra Độ chệch bằng cách che khuất một số cấu trúc của _f_ ( _X_ ). Trong Chương 5, chúng ta sẽ giới thiệu một số cách tiếp cận để ước lượng tỷ lệ lỗi kiểm tra. Các phương pháp này có thể được sử dụng để xác định giá trị tối ưu của _K_ trong hồi quy KNN. 

Trong bối cảnh nào thì một phương pháp tham số như hồi quy tuyến tính bình phương tối thiểu sẽ có hiệu suất vượt trội hơn một phương pháp phi tham số như hồi quy KNN? Câu trả lời rất đơn giản: _phương pháp tham số sẽ có hiệu suất tốt hơn phương pháp phi tham số nếu dạng tham số đã được chọn gần với dạng thực tế của f_. Hình 3.17 cung cấp một ví dụ với dữ liệu được tạo ra 

3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors 107 

từ một mô hình hồi quy tuyến tính một chiều. Các đường thẳng nét liền màu đen biểu diễn _f_ ( _X_ ), trong khi các đường cong màu xanh lam tương ứng với các đường khớp KNN sử dụng _K_ = 1 và _K_ = 9. Trong trường hợp này, các dự đoán cho _K_ = 1 quá biến động, trong khi đường khớp _K_ = 9 mượt mà hơn nhiều và gần gũi hơn với _f_ ( _X_ ). Tuy nhiên, vì mối quan hệ thực tế là tuyến tính, nên thật khó để một phương pháp phi tham số cạnh tranh được với hồi quy tuyến tính: một phương pháp phi tham số phải chịu một chi phí về Phương sai mà không được bù đắp bởi sự giảm bớt về Độ chệch. Đường nét đứt màu xanh lam trong hình bên trái của Hình 3.18 biểu diễn đường khớp hồi quy tuyến tính cho cùng dữ liệu. Nó gần như hoàn hảo. Hình bên phải của Hình 3.18 tiết lộ rằng hồi quy tuyến tính có hiệu suất tốt hơn KNN cho dữ liệu này. Đường nét liền màu xanh lá cây, được vẽ dưới dạng một hàm của 1 _/K_ , biểu diễn sai số toàn phương trung bình (MSE) trên tập kiểm tra cho KNN. Các sai số KNN cao hơn hẳn so với đường nét đứt màu đen, đó là MSE kiểm tra cho hồi quy tuyến tính. Khi giá trị của _K_ lớn, KNN chỉ có hiệu suất kém hơn hồi quy bình phương tối thiểu một chút về mặt MSE. Nó hoạt động kém hơn rất nhiều khi _K_ nhỏ. 

Trong thực tế, mối quan hệ thực sự giữa _X_ và _Y_ hiếm khi hoàn toàn tuyến tính. Hình 3.19 kiểm tra hiệu suất tương đối của hồi quy bình phương tối thiểu và KNN dưới các mức độ phi tuyến ngày càng tăng trong mối quan hệ giữa _X_ và _Y_ . Ở hàng trên cùng, mối quan hệ thực sự gần như tuyến tính. Trong trường hợp này, chúng ta thấy rằng MSE kiểm tra cho hồi quy tuyến tính vẫn vượt trội hơn so với KNN ở các giá trị _K_ thấp. Tuy nhiên, đối với _K ≥_ 4, KNN hoạt động tốt hơn hồi quy tuyến tính. Hàng thứ hai minh họa một sự sai lệch đáng kể hơn nhiều so với tính tuyến tính. Trong tình huống này, KNN hoạt động tốt hơn hẳn so với hồi quy tuyến tính ở tất cả các giá trị của _K_ . Lưu ý rằng khi mức độ phi tuyến tăng lên, có ít sự thay đổi trong MSE tập kiểm tra cho phương pháp KNN phi tham số, nhưng lại có một sự gia tăng lớn ở MSE tập kiểm tra của hồi quy tuyến tính. 

Các Hình 3.18 và 3.19 hiển thị các tình huống trong đó KNN hoạt động kém hơn một chút so với hồi quy tuyến tính khi mối quan hệ là tuyến tính, nhưng lại tốt hơn rất nhiều so với hồi quy tuyến tính đối với các tình huống phi tuyến. Trong một tình huống thực tế mà mối quan hệ thực sự là chưa biết, người ta có thể nghi ngờ rằng KNN nên được ưu tiên hơn hồi quy tuyến tính bởi vì trong trường hợp tồi tệ nhất, nó sẽ chỉ kém hơn một chút so với hồi quy tuyến tính nếu mối quan hệ thực sự là tuyến tính, và có thể mang lại kết quả tốt hơn đáng kể nếu mối quan hệ thực sự là phi tuyến. Nhưng trong thực tế, ngay cả khi mối quan hệ thực sự là phi tuyến cao, KNN vẫn có thể cung cấp các kết quả kém hơn so với hồi quy tuyến tính. Cụ thể, cả Hình 3.18 và 3.19 đều minh họa các bối cảnh với _p_ = 1 Biến dự báo. Nhưng trong các không gian có số chiều cao hơn, KNN thường có hiệu suất kém hơn hồi quy tuyến tính. 

Hình 3.20 xem xét tình huống có tính phi tuyến mạnh tương tự như ở hàng thứ hai của Hình 3.19, ngoại trừ việc chúng ta đã thêm các Biến dự báo _nhiễu_ bổ sung không có liên quan tới Biến phản hồi. Khi _p_ = 1 hoặc _p_ = 2, KNN hoạt động tốt hơn hồi quy tuyến tính. Nhưng đối với _p_ = 3, kết quả là hỗn hợp, và đối với _p ≥_ 4, hồi quy tuyến tính ưu việt hơn KNN. Thực tế, sự gia tăng về số chiều chỉ gây ra một sự suy giảm nhỏ trong MSE tập kiểm tra của hồi quy tuyến tính, nhưng nó đã gây ra mức tăng gấp hơn mười lần về MSE cho 

108 3. Linear Regression 


![](images/chapter_3.pdf-0050-01.png)


**HÌNH 3.17.** _Các biểu đồ của f_<sup>ˆ</sup> ( _X_ ) _sử dụng hồi quy KNN trên một tập dữ liệu một chiều với_ 50 _quan sát. Mối quan hệ thực sự được biểu diễn bởi đường thẳng nét liền màu đen._ Trái: _Đường cong màu xanh lam tương ứng với K_ = 1 _và nội suy (tức là đi trực tiếp qua) dữ liệu huấn luyện._ Phải: _Đường cong màu xanh lam tương ứng với K_ = 9 _, và biểu diễn một đường khớp mượt mà hơn._ 


![](images/chapter_3.pdf-0050-03.png)


**HÌNH 3.18.** _Cùng một tập dữ liệu được hiển thị trong Hình 3.17 được khảo sát thêm._ Trái: _Đường nét đứt màu xanh lam là đường bình phương tối thiểu cho dữ liệu. Vì f_ ( _X_ ) _trên thực tế là tuyến tính (được hiển thị dưới dạng đường màu đen), đường hồi quy bình phương tối thiểu cung cấp một ước lượng rất tốt cho f_ ( _X_ ) _._ Phải: _Đường nằm ngang nét đứt biểu diễn MSE kiểm tra bình phương tối thiểu, trong khi đường nét liền màu xanh lá cây tương ứng với MSE cho KNN dưới dạng một hàm của_ 1 _/K (trên thang logarit). Hồi quy tuyến tính đạt được MSE kiểm tra thấp hơn so với hồi quy KNN, vì f_ ( _X_ ) _thực tế là tuyến tính. Đối với hồi quy KNN, kết quả tốt nhất xảy ra với một giá trị rất lớn của K, tương ứng với một giá trị nhỏ của_ 1 _/K._ 

3.5 Comparison of Linear Regression with _K_ -Nearest Neighbors 

109 


![](images/chapter_3.pdf-0051-02.png)


**HÌNH 3.19.** Trên cùng bên trái: _Trong một bối cảnh với một mối quan hệ phi tuyến nhẹ giữa X và Y (đường nét liền màu đen), các đường khớp KNN với K_ = 1 _(màu xanh lam) và K_ = 9 _(màu đỏ) được hiển thị._ Trên cùng bên phải: _Đối với dữ liệu phi tuyến nhẹ, MSE trên tập kiểm tra đối với hồi quy bình phương tối thiểu (đường nằm ngang màu đen) và KNN với các giá trị khác nhau của_ 1 _/K (màu xanh lá cây) được hiển thị._ Dưới cùng bên trái và Dưới cùng bên phải: _Tương tự như bảng trên cùng, nhưng với một mối quan hệ phi tuyến tính mạnh giữa X và Y ._ 

110 3. Linear Regression 


![](images/chapter_3.pdf-0052-01.png)


**HÌNH 3.20.** _MSE kiểm tra cho hồi quy tuyến tính (các đường nét đứt màu đen) và KNN (các đường cong màu xanh lá cây) khi số lượng biến p tăng lên. Hàm số thực tế là phi tuyến ở biến đầu tiên, giống như ở hình dưới của Hình 3.19, và không phụ thuộc vào các biến bổ sung. Hiệu suất của hồi quy tuyến tính suy giảm từ từ với sự hiện diện của các biến nhiễu bổ sung này, trong khi hiệu suất của KNN suy giảm nhanh hơn rất nhiều khi p tăng._ 

KNN. Sự suy giảm hiệu suất này khi số chiều tăng lên là một vấn đề phổ biến đối với KNN, và là kết quả của việc trong các không gian có số chiều cao hơn thì thực chất là có sự sụt giảm về kích thước mẫu. Trong tập dữ liệu này có 50 quan sát huấn luyện; khi _p_ = 1, điều này cung cấp đủ thôngChứng này cung cấp đủ thông tin để ước lượng chính xác _f_ ( _X_ ). Tuy nhiên, việc trải đều 50 quan sát trên _p_ = 20 chiều dẫn đến một hiện tượng trong đó một quan sát nhất định không có các _láng giềng gần_ — đây được gọi là _lời nguyền của số chiều_ (curse of dimensionality). Tức là, _K_ quan sát gần nhất với một quan sát kiểm tra _x_ 0 nhất định có thể ở rất xa so với _x_ 0 trong không gian _p_ chiều khi _p_ lớn, dẫn đến một dự đoán rất kém về _f_ ( _x_ 0) và do đó một đường khớp KNN kém. Theo nguyên tắc chung, các phương pháp tham số sẽ có xu hướng hoạt động tốt hơn các cách tiếp cận phi tham số khi có một số lượng nhỏ các quan sát trên mỗi Biến dự báo. 

Ngay cả khi số chiều nhỏ, chúng ta có thể thích hồi quy tuyến tính hơn KNN từ quan điểm diễn giải. Nếu MSE kiểm tra của KNN chỉ thấp hơn một chút so với MSE kiểm tra của hồi quy tuyến tính, chúng ta có thể sẵn sàng từ bỏ một chút độ chính xác dự đoán để đổi lấy một mô hình đơn giản có thể được mô tả theo một vài hệ số, và cho phép có sẵn các giá trị _p_. 


## 3.6 Thực hành: Hồi quy tuyến tính (Linear Regression) 

### _3.6.1 Các thư viện (Libraries)_ 

Hàm `library()` được sử dụng để tải các _thư viện_ (libraries), hoặc các nhóm hàm `library()` và tập dữ liệu không được bao gồm trong bản phân phối `R` cơ bản. Các hàm cơ bản để thực hiện hồi quy tuyến tính bình phương tối thiểu (least squares linear regression) và các phân tích đơn giản khác đi kèm theo tiêu chuẩn với bản phân phối cơ bản, nhưng các hàm phức tạp hơn yêu cầu 

3.6 Thực hành: Hồi quy tuyến tính 111 

các thư viện bổ sung. Ở đây chúng ta tải gói `MASS`, đây là một bộ sưu tập rất lớn các tập dữ liệu và hàm. Chúng ta cũng tải gói `ISLR2`, bao gồm các tập dữ liệu liên quan đến cuốn sách này. 

###### <mark>`> library(MASS) > library(ISLR2)`</mark> 

Nếu bạn nhận được thông báo lỗi khi tải bất kỳ thư viện nào trong số này, điều đó có thể chỉ ra rằng thư viện tương ứng chưa được cài đặt trên hệ thống của bạn. Một số thư viện, chẳng hạn như `MASS`, đi kèm với `R` và không cần phải cài đặt riêng trên máy tính của bạn. Tuy nhiên, các gói khác, chẳng hạn như `ISLR2`, phải được tải xuống trong lần đầu tiên chúng được sử dụng. Điều này có thể được thực hiện trực tiếp từ bên trong `R`. Ví dụ, trên hệ thống Windows, hãy chọn tùy chọn `Install package` trong thẻ `Packages`. Sau khi bạn chọn bất kỳ trang web máy chủ phản chiếu (mirror site) nào, danh sách các gói có sẵn sẽ xuất hiện. Chỉ cần chọn gói bạn muốn cài đặt và `R` sẽ tự động tải xuống gói đó. Ngoài ra, điều này có thể được thực hiện tại dòng lệnh `R` thông qua `install.packages("ISLR2")`. Việc cài đặt này chỉ cần thực hiện trong lần đầu tiên bạn sử dụng một gói. Tuy nhiên, hàm `library()` phải được gọi trong mỗi phiên làm việc của `R`. 

### _3.6.2 Hồi quy tuyến tính đơn (Simple Linear Regression)_ 

Thư viện `ISLR2` chứa tập dữ liệu `Boston`, ghi lại `medv` (giá trị nhà trung vị) cho 506 khu vực điều tra dân số ở Boston. Chúng ta sẽ tìm cách dự đoán `medv` sử dụng 12 biến dự báo (predictors) như `rm` (số phòng trung bình mỗi ngôi nhà), `age` (tỷ lệ các căn hộ do chủ sở hữu ở được xây dựng trước năm 1940) và `lstat` (tỷ lệ phần trăm hộ gia đình có tình trạng kinh tế xã hội thấp). 

###### <mark>`> head(Boston)`</mark> 

|`crim `|`zn `|`in`|`dus chas`|`nox`|**`rm`**|`age`<br>`dis `|`rad `|`tax`|
|---|---|---|---|---|---|---|---|---|
|`1 0.00632 `|`18`|`2`|`.31`<br>`0 `|`0.538 `|`6.575 `|`65.2 4.0900`|`1 `|`296`|
|`2 0.02731`|`0`|`7`|`.07`<br>`0 `|`0.469 `|`6.421 `|`78.9 4.9671`|`2 `|`242`|
|`3 0.02729`|`0`|`7`|`.07`<br>`0 `|`0.469 `|`7.185 `|`61.1 4.9671`|`2 `|`242`|
|`4 0.03237`|`0`|`2`|`.18`<br>`0 `|`0.458 `|`6.998 `|`45.8 6.0622`|`3 `|`222`|
|`5 0.06905`|`0`|`2`|`.18`<br>`0 `|`0.458 `|`7.147 `|`54.2 6.0622`|`3 `|`222`|
|`6 0.02985`|`0`|`2`|`.18`<br>`0 `|`0.458 `|`6.430 `|`58.7 6.0622`|`3 `|`222`|
|`ptratio `|`lst`|`at `|`medv`||||||
|`1`<br>`15.3`|`4.`|`98 `|`24.0`||||||
|`2`<br>`17.8`|`9.`|`14 `|`21.6`||||||
|`3`<br>`17.8`|`4.`|`03 `|`34.7`||||||
|`4`<br>`18.7`|`2.`|`94 `|`33.4`||||||
|`5`<br>`18.7`|`5.`|`33 `|`36.2`||||||
|`6`<br>`18.7`|`5.`|`21 `|`28.7`||||||

Để tìm hiểu thêm về tập dữ liệu, chúng ta có thể gõ `?Boston`. 

Chúng ta sẽ bắt đầu bằng cách sử dụng hàm `lm()` để khớp một mô hình hồi quy tuyến tính đơn `lm()`, với `medv` là biến phản hồi (response) và `lstat` là biến dự báo (predictor). Cú pháp cơ bản là `lm(y` _∼_ `x, data)`, trong đó `y` là biến phản hồi, `x` là biến dự báo, và `data` là tập dữ liệu mà hai biến này được lưu trữ. 

112 3. Hồi quy tuyến tính 

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`lstat) Error in`</mark> **<mark>`eval`</mark>** <mark>`(expr, envir, enclos) : Object`</mark> **<mark>`"medv"`</mark>** <mark>`not found`</mark> 

Lệnh này gây ra lỗi vì `R` không biết tìm các biến `medv` và `lstat` ở đâu. Dòng tiếp theo báo cho `R` biết rằng các biến nằm trong `Boston`. Nếu chúng ta đính kèm (attach) `Boston`, dòng đầu tiên hoạt động tốt vì `R` hiện đã nhận dạng được các biến. 

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`lstat, data = Boston) > attach(Boston) >`</mark> **<mark>`lm`</mark>** <mark>`.fit <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`lstat)`</mark> 

Nếu chúng ta gõ `lm.fit`, một số thông tin cơ bản về mô hình sẽ được xuất ra. Để biết thêm thông tin chi tiết, chúng ta sử dụng `summary(lm.fit)`. Điều này cung cấp cho chúng ta các giá trị _p_ (p-values) và sai số chuẩn (standard errors) cho các hệ số, cũng như thống kê _R_<sup>2</sup> và thống kê _F_ (F-statistic) cho mô hình. 

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit`</mark> **<mark>`Call`</mark>** <mark>`:`</mark> **<mark>`lm`</mark>** <mark>`(`</mark> **<mark>`formula`</mark>** <mark>`= medv`</mark> _<mark>∼</mark>_ <mark>`lstat) Coefficients: (Intercept) lstat 34.55 -0.95 > summary(`</mark> **<mark>`lm`</mark>** <mark>`.fit)`</mark> **<mark>`Call`</mark>** <mark>`:`</mark> **<mark>`lm`</mark>** <mark>`(`</mark> **<mark>`formula`</mark>** <mark>`= medv`</mark> _<mark>∼</mark>_ <mark>`lstat) Residuals: Min 1`</mark> **<mark>`Q`</mark>** <mark>`Median 3`</mark> **<mark>`Q`</mark>** <mark>`Max -15.17 -3.99 -1.32 2.03 24.50 Coefficients: Estimate Std. Error t value Pr(>|t|) (Intercept) 34.5538 0.5626 61.4 <2e-16 *** lstat -0.9500 0.0387 -24.5 <2e-16 *** --Signif.`</mark> **<mark>`codes`</mark>** <mark>`: 0 *** 0.001 ** 0.01 * 0.05 . 0.1 1 Residual standard error: 6.22`</mark> **<mark>`on`</mark>** <mark>`504 degrees of freedom Multiple R-squared: 0.544, Adjusted R-squared: 0.543 F-statistic: 602`</mark> **<mark>`on`</mark>** <mark>`1 and 504 DF, p-value: < 2e-16`</mark> 

Chúng ta có thể sử dụng hàm `names()` để tìm hiểu xem những mẩu thông tin nào khác được lưu trữ trong `lm.fit`. Mặc dù chúng ta có thể trích xuất các đại lượng này bằng tên — ví dụ: `lm.fit$coefficients` — nhưng an toàn hơn là sử dụng các hàm trích xuất như `coef()` để truy cập chúng. 

```
names()
```

```
coef()
```

```
>names(lm.fit)
[1]"coefficients""residuals""effects"
[4]"rank""fitted.values""assign"
```

3.6 Thực hành: Hồi quy tuyến tính 

113 

|**`[7] "qr"`**|**`"df.residual"`**|**`"xlevels"`**|
|---|---|---|
|**`[10] "call"`**|**`"terms"`**|**`"model"`**|
|`> coef(`**`lm`**`.fit)`|||
|`(Intercept)`|`lstat`||
|`34.55`|`-0.95`||



Để có được khoảng tin cậy (confidence interval) cho các ước lượng hệ số, chúng ta có thể sử dụng lệnh `confint()`. 

```
confint()
```

```
>confint(lm.fit)
2.5%97.5%
(Intercept)33.4535.659
lstat-1.03-0.874
```

Hàm `predict()` có thể được sử dụng để tạo ra các khoảng tin cậy và các khoảng dự đoán `predict()` cho việc dự đoán `medv` đối với một giá trị cho trước của `lstat`. 

```
>predict(lm.fit,data.frame(lstat=(c(5,10,15))),
interval="confidence")
fitlwrupr
129.8029.0130.60
225.0524.4725.63
320.3019.7320.87
>predict(lm.fit,data.frame(lstat=(c(5,10,15))),
interval="prediction")
fitlwrupr
129.8017.56642.04
225.0512.82837.28
320.308.07832.53
```

Chẳng hạn, khoảng tin cậy 95% liên kết với một giá trị `lstat` bằng 10 là (24 _._ 47 _,_ 25 _._ 63), và khoảng dự đoán 95% là (12 _._ 828 _,_ 37 _._ 28). Đúng như kỳ vọng, các khoảng tin cậy và khoảng dự đoán được tập trung xung quanh cùng một điểm (một giá trị được dự đoán là 25 _._ 05 cho `medv` khi `lstat` bằng 10), nhưng các khoảng dự đoán thì rộng hơn đáng kể. 

Bây giờ chúng ta sẽ vẽ đồ thị `medv` và `lstat` cùng với đường hồi quy bình phương tối thiểu bằng cách sử dụng các hàm `plot()` và `abline()`. 

```
abline()
```

```
>plot(lstat,medv)
>abline(lm.fit)
```

Có một số bằng chứng về tính phi tuyến (non-linearity) trong mối quan hệ giữa `lstat` và `medv`. Chúng ta sẽ khám phá vấn đề này sau trong phần thực hành này. 

Hàm `abline()` có thể được sử dụng để vẽ bất kỳ đường thẳng nào, không chỉ đường hồi quy bình phương tối thiểu. Để vẽ một đường thẳng với tung độ gốc (intercept) `a` và độ dốc (slope) `b`, chúng ta gõ `abline(a, b)`. Dưới đây chúng ta thử nghiệm với một số thiết lập bổ sung để vẽ các đường và các điểm. Lệnh `lwd = 3` làm cho độ rộng của đường hồi quy tăng lên theo hệ số 3; điều này cũng hoạt động đối với các hàm `plot()` và `lines()`. Chúng ta cũng có thể sử dụng tùy chọn `pch` để tạo ra các ký hiệu vẽ đồ thị khác nhau. 

```
>abline(lm.fit,lwd=3)
```

```
>abline(lm.fit,lwd=3,col="red")
```

114 3. Hồi quy tuyến tính 

```
>plot(lstat,medv,col="red")
```

```
>plot(lstat,medv,pch=20)
>plot(lstat,medv,pch="+")
>plot(1:20,1:20,pch=1:20)
```

Tiếp theo chúng ta xem xét một số biểu đồ chẩn đoán (diagnostic plots), một số trong đó đã được thảo luận trong Mục 3.3.3. Bốn biểu đồ chẩn đoán được tự động tạo ra bằng cách áp dụng hàm `plot()` trực tiếp vào đầu ra từ `lm()`. Nói chung, lệnh này sẽ tạo ra từng biểu đồ một, và nhấn _Enter_ sẽ tạo ra biểu đồ tiếp theo. Tuy nhiên, thường thì việc xem cả bốn biểu đồ cùng nhau sẽ thuận tiện hơn. Chúng ta có thể đạt được điều này bằng cách sử dụng các hàm `par()` và `mfrow()`, thông báo cho `R par()` chia màn hình hiển thị thành các bảng phụ (panels) riêng biệt để nhiều biểu đồ có thể được xem đồng thời. Ví dụ, `par(mfrow = c(2, 2))` chia vùng vẽ đồ thị thành một lưới 2 _×_ 2 bảng phụ. 

```
mfrow()
```

```
>par(mfrow=c(2,2))
>plot(lm.fit)
```

Ngoài ra, chúng ta có thể tính toán các phần dư (residuals) từ một kết quả khớp hồi quy tuyến tính bằng cách sử dụng hàm `residuals()`. Hàm `rstudent()` sẽ trả về các phần dư được student hóa (studentized residuals) `residuals()`, và chúng ta có thể sử dụng hàm này để vẽ biểu đồ các phần dư `rstudent()` theo các giá trị được khớp (fitted values). 

```
>plot(predict(lm.fit),residuals(lm.fit))
```

```
>plot(predict(lm.fit),rstudent(lm.fit))
```

Dựa trên các biểu đồ phần dư, có một số bằng chứng về tính phi tuyến. Các thống kê đòn bẩy (leverage statistics) có thể được tính toán cho bất kỳ số lượng biến dự báo nào bằng cách sử dụng hàm `hatvalues()`. 

```
hatvalues()
```

```
>plot(hatvalues(lm.fit))
>which.max(hatvalues(lm.fit))
375
```

Hàm `which.max()` xác định chỉ mục (index) của phần tử lớn nhất của một vector `which.max()`. Trong trường hợp này, nó cho chúng ta biết quan sát nào có thống kê đòn bẩy lớn nhất. 

### _3.6.3 Hồi quy tuyến tính bội (Multiple Linear Regression)_ 

Để khớp một mô hình hồi quy tuyến tính bội bằng cách sử dụng bình phương tối thiểu, một lần nữa chúng ta sử dụng hàm `lm()`. Cú pháp `lm(y` _∼_ `x1 + x2 + x3)` được sử dụng để khớp một mô hình với ba biến dự báo, `x1`, `x2`, và `x3`. Hàm `summary()` bây giờ xuất ra các hệ số hồi quy cho tất cả các biến dự báo. 

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`lstat + age, data = Boston)`</mark> 

```
>summary(lm.fit)
```

**<mark>`Call`</mark>** <mark>`:`</mark> **<mark>`lm`</mark>** <mark>`(`</mark> **<mark>`formula`</mark>** <mark>`= medv`</mark> _<mark>∼</mark>_ <mark>`lstat + age, data = Boston)`</mark> 

```
Residuals:
```

3.6 Thực hành: Hồi quy tuyến tính 115 

```
Min1QMedian3QMax
-15.98-3.98-1.281.9723.16
Coefficients:
EstimateStd.ErrortvaluePr(>|t|)
(Intercept)33.22280.730845.46<2e-16***
lstat-1.03210.0482-21.42<2e-16***
age0.03450.01222.830.0049**
---
Signif.codes:0***0.001**0.01*0.05.0.11
Residualstandarderror:6.17on503degreesoffreedom
MultipleR-squared:0.551,AdjustedR-squared:0.549
F-statistic:309on2and503DF,p-value:<2e-16
```

Tập dữ liệu `Boston` chứa 12 biến, và do đó sẽ rất cồng kềnh nếu phải gõ tất cả các biến này để thực hiện một phép hồi quy sử dụng tất cả các biến dự báo. Thay vào đó, chúng ta có thể sử dụng cú pháp viết tắt (short-hand) sau: 

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`., data = Boston) > summary(`</mark> **<mark>`lm`</mark>** <mark>`.fit)`</mark> 

|**`Call`**`:`||||
|---|---|---|---|
|**`lm`**`(`**`formula`** `= medv` _∼_`.`|`, data = Bo`|`ston)`||
|`Residuals:`||||
|`Min`<br>`1`**`Q`**<br>`Medi`|`an`<br>`3`**`Q`**|`Max`||
|`-15.130`<br>`-2.767`<br>`-0.5`|`81`<br>`1.941`|`26.253`||
|`Coefficients:`||||
|`Estimate `|`Std. Error `|`t value `|`Pr(>|t|)`|
|`(Intercept)`<br>`41.61727`|`4.93604`|`8.43`|`3.8e-16 ***`|
|`crim`<br>`-0.12139`|`0.03300`|`-3.68`|`0.00026 ***`|
|`zn`<br>`0.04696`|`0.01388`|`3.38`|`0.00077 ***`|
|`indus`<br>`0.01347`|`0.06214`|`0.22`|`0.82852`|
|`chas`<br>`2.83999`|`0.87001`|`3.26`|`0.00117 **`|
|`nox`<br>`-18.75802`|`3.85135`|`-4.87`|`1.5e-06 ***`|
|**`rm`**<br>`3.65812`|`0.42025`|`8.70`|`< 2e-16 ***`|
|`age`<br>`0.00361`|`0.01333`|`0.27`|`0.78659`|
|`dis`<br>`-1.49075`|`0.20162`|`-7.39`|`6.2e-13 ***`|
|`rad`<br>`0.28940`|`0.06691`|`4.33`|`1.8e-05 ***`|
|`tax`<br>`-0.01268`|`0.00380`|`-3.34`|`0.00091 ***`|
|`ptratio`<br>`-0.93753`|`0.13221`|`-7.09`|`4.6e-12 ***`|
|`lstat`<br>`-0.55202`<br>`---`|`0.05066`|`-10.90`|`< 2e-16 ***`|
|`Signif.` **`codes`**`:`<br>`0 *** `|`0.001 ** 0`|`.01 * 0.0`|`5 . 0.1`<br>`1`|
|`Residual standard err`|`or: 4.8` **`on`**|`493 degre`|`es of freedom`|
|`Multiple R-squared:`<br>|`0.734,`<br>|`Adjusted `|`R-squared:`<br>`0.728`|
|`F-statistic:`<br>`114` **`on`**|`12 and 493 `|`DF,`<br>`p-va`|`lue: < 2e-16`|

Chúng ta có thể truy cập các thành phần riêng lẻ của một đối tượng tóm tắt bằng tên (gõ `?summary.lm` để xem những gì có sẵn). Do đó, `summary(lm.fit)$r.sq` cung cấp cho chúng ta _R_<sup>2</sup>, và `summary(lm.fit)$sigma` cung cấp cho chúng ta RSE (Residual Standard Error - Sai số chuẩn phần dư). Hàm `vif() vif()` 

116 3. Hồi quy tuyến tính 

(từ gói `car`) có thể được sử dụng để tính toán các nhân tử lạm phát phương sai (variance inflation factors - VIF). Hầu hết các VIF đều từ thấp đến trung bình đối với dữ liệu này. Gói `car` không thuộc bản cài đặt cơ bản của `R` nên nó phải được tải xuống trong lần đầu tiên bạn sử dụng nó thông qua hàm `install.packages()` trong `R`. 

|`> library`<br>`> vif(`**`lm`**`.`|`(car)`<br>`fit)`|||||||
|---|---|---|---|---|---|---|---|
|`crim`|`zn`|`indus`|`chas`|`nox`|**`rm`**|`age`|`dis`|
|`1.77`|`2.30`|`3.99`|`1.07`|`4.37`|`1.91`|`3.09`|`3.95`|
|`rad`|`tax `|`ptratio`|`lstat`|||||
|`7.45`|`9.00`|`1.80`|`2.87`|||||



Điều gì sẽ xảy ra nếu chúng ta muốn thực hiện một phép hồi quy sử dụng tất cả các biến ngoại trừ một biến? Ví dụ, trong đầu ra hồi quy ở trên, `age` có một giá trị _p_ cao. Vì vậy, chúng ta có thể muốn chạy một phép hồi quy loại trừ biến dự báo này. Cú pháp sau đây dẫn đến một phép hồi quy sử dụng tất cả các biến dự báo ngoại trừ `age`. 

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit1 <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`. - age, data = Boston) > summary(`</mark> **<mark>`lm`</mark>** <mark>`.fit1) ...`</mark> 

Ngoài ra, hàm `update()` có thể được sử dụng. 

```
update()
```

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit1 <- update(`</mark> **<mark>`lm`</mark>** <mark>`.fit,`</mark> _<mark>∼</mark>_ <mark>`. - age)`</mark>


### _3.6.4 Các thuật ngữ tương tác (Interaction Terms)_

Rất dễ dàng để đưa các thuật ngữ tương tác vào một mô hình tuyến tính bằng cách sử dụng hàm `lm()`. Cú pháp `lstat:age` yêu cầu `R` bao gồm một thuật ngữ tương tác giữa `lstat` và `age`. Cú pháp `lstat * age` đồng thời bao gồm `lstat`, `age` và thuật ngữ tương tác `lstat` _×_ `age` như là các biến dự báo (predictors); đây là cách viết rút gọn cho `lstat + age + lstat:age`.

<mark>`> summary(lm(medv`</mark> _<mark>∼</mark>_ <mark>`lstat * age, data = Boston))`</mark> 

**<mark>`Call`</mark>** <mark>`:`</mark> **<mark>`lm`</mark>** <mark>`(`</mark> **<mark>`formula`</mark>** <mark>`= medv`</mark> _<mark>∼</mark>_ <mark>`lstat * age, data = Boston) Residuals: Min 1`</mark> **<mark>`Q`</mark>** <mark>`Median 3`</mark> **<mark>`Q`</mark>** <mark>`Max -15.81 -4.04 -1.33 2.08 27.55 Coefficients: Estimate Std. Error t value Pr(>|t|) (Intercept) 36.088536 1.469835 24.55 < 2e-16 *** lstat -1.392117 0.167456 -8.31 8.8e-16 *** age -0.000721 0.019879 -0.04 0.971 lstat:age 0.004156 0.001852 2.24 0.025 * --Signif.`</mark> **<mark>`codes`</mark>** <mark>`: 0 *** 0.001 ** 0.01 * 0.05 . 0.1 1 Residual standard error: 6.15`</mark> **<mark>`on`</mark>** <mark>`502 degrees of freedom`</mark> 

3.6 Lab: Linear Regression 

117 

```
MultipleR-squared:0.556,AdjustedR-squared:0.553
F-statistic:209on3and502DF,p-value:<2e-16
```

### _3.6.5 Các phép biến đổi phi tuyến tính của biến dự báo (Non-linear Transformations of the Predictors)_

Hàm `lm()` cũng có thể chứa các phép biến đổi phi tuyến tính của các biến dự báo. Ví dụ, với một biến dự báo _X_, ta có thể tạo một biến dự báo _X_<sup>2</sup> bằng cách sử dụng `I(X^2)`. Hàm `I()` là cần thiết vì ký hiệu `^` có một ý nghĩa đặc biệt trong một đối tượng công thức (formula object); việc bao bọc như chúng ta làm cho phép cách sử dụng tiêu chuẩn trong `R`, đó là nâng `X` lên lũy thừa `2`. Bây giờ chúng ta thực hiện hồi quy của `medv` theo `lstat` và `lstat`<sup>2</sup>.

```
I()
```

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit2 <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`lstat + I(lstat^2)) > summary(`</mark> **<mark>`lm`</mark>** <mark>`.fit2)`</mark> 

**<mark>`Call`</mark>** <mark>`:`</mark> **<mark>`lm`</mark>** <mark>`(`</mark> **<mark>`formula`</mark>** <mark>`= medv`</mark> _<mark>∼</mark>_ <mark>`lstat +`</mark> **<mark>`I`</mark>** <mark>`(lstat^2)) Residuals: Min 1`</mark> **<mark>`Q`</mark>** <mark>`Median 3`</mark> **<mark>`Q`</mark>** <mark>`Max -15.28 -3.83 -0.53 2.31 25.41 Coefficients: Estimate Std. Error t value Pr(>|t|) (Intercept) 42.86201 0.87208 49.1 <2e-16 *** lstat -2.33282 0.12380 -18.8 <2e-16 ***`</mark> **<mark>`I(lstat^2)`</mark>** <mark>`0.04355 0.00375 11.6 <2e-16 *** --Signif.`</mark> **<mark>`codes`</mark>** <mark>`: 0 *** 0.001 ** 0.01 * 0.05 . 0.1 1`</mark> 

```
Residualstandarderror:5.52on503degreesoffreedom
MultipleR-squared:0.641,AdjustedR-squared:0.639
F-statistic:449on2and503DF,p-value:<2e-16
```

Giá trị _p_ (p-value) gần bằng không liên kết với thuật ngữ bậc hai cho thấy rằng nó dẫn đến một mô hình cải tiến. Chúng ta sử dụng hàm `anova()` để định lượng thêm mức độ mà hồi quy bậc hai vượt trội so với hồi quy tuyến tính.

```
anova()
```

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`lstat) > anova(`</mark> **<mark>`lm`</mark>** <mark>`.fit,`</mark> **<mark>`lm`</mark>** <mark>`.fit2) Analysis of Variance Table Model 1: medv`</mark> _<mark>∼</mark>_ <mark>`lstat Model 2: medv`</mark> _<mark>∼</mark>_ <mark>`lstat +`</mark> **<mark>`I`</mark>** <mark>`(lstat^2) Res.Df RSS Df Sum of Sq F Pr(>F) 1 504 19472 2 503 15347 1 4125 135 <2e-16 *** --Signif.`</mark> **<mark>`codes`</mark>** <mark>`: 0 *** 0.001 ** 0.01 * 0.05 . 0.1 1`</mark> 

Ở đây Model 1 đại diện cho mô hình con tuyến tính chỉ chứa một biến dự báo, `lstat`, trong khi Model 2 tương ứng với mô hình bậc hai lớn hơn có hai

118 3. Linear Regression 

biến dự báo, `lstat` và `lstat`<sup>2</sup>. Hàm `anova()` thực hiện một kiểm định giả thuyết so sánh hai mô hình. Giả thuyết không (null hypothesis) là hai mô hình khớp với dữ liệu tốt như nhau, và giả thuyết thay thế (alternative hypothesis) là mô hình đầy đủ vượt trội hơn. Ở đây giá trị thống kê _F_ (F-statistic) là 135 và giá trị _p_ (p-value) liên quan gần như bằng không. Điều này cung cấp bằng chứng rất rõ ràng rằng mô hình chứa các biến dự báo `lstat` và `lstat`<sup>2</sup> vượt trội hơn hẳn so với mô hình chỉ chứa biến dự báo `lstat`. Điều này không có gì đáng ngạc nhiên, vì trước đó chúng ta đã thấy bằng chứng về tính phi tuyến tính trong mối quan hệ giữa `medv` và `lstat`. Nếu chúng ta gõ

```
>par(mfrow=c(2,2))
>plot(lm.fit2)
```

sau đó chúng ta thấy rằng khi thuật ngữ `lstat`<sup>2</sup> được đưa vào mô hình, có rất ít mẫu có thể nhận ra được trong các phần dư.

Để tạo một hồi quy bậc ba (cubic fit), chúng ta có thể bao gồm một biến dự báo có dạng `I(X^3)`. Tuy nhiên, cách tiếp cận này có thể bắt đầu trở nên cồng kềnh đối với các đa thức bậc cao hơn. Một cách tiếp cận tốt hơn liên quan đến việc sử dụng hàm `poly()` để tạo đa thức bên trong `lm()`. Ví dụ, lệnh sau đây tạo ra một hồi quy đa thức bậc năm:

```
poly()
```

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit5 <- lm(medv`</mark> _<mark>∼</mark>_ <mark>`poly(lstat, 5)) > summary(`</mark> **<mark>`lm`</mark>** <mark>`.fit5)`</mark> 

```
Call:
```

**<mark>`lm`</mark>** <mark>`(`</mark> **<mark>`formula`</mark>** <mark>`= medv`</mark> _<mark>∼</mark>_ **<mark>`poly`</mark>** <mark>`(lstat, 5))`</mark> 

|`Residuals:`<br><br>|||||
|---|---|---|---|---|
|`Min`<br>`1`**`Q`**<br>`-13.543`<br>`-3.104`|`Median`<br>`-0.705`|`3`**`Q`**<br>`2.084`<br>`27`|`Max`<br>`.115`||
|`Coefficients:`|||||
||`Estimate `|`Std. Error `|`t value `|`Pr(>|t|)`|
|`(Intercept)`|`22.533`|`0.232`|`97.20`|`< 2e-16 ***`|
|**`poly(lstat, 5)1 `**|**`-152.460`**|**`5.215`**|**`-29.24`**|**`< 2e-16 ***`**|
|**`poly(lstat, 5)2`**|**`64.227`**|**`5.215`**|**`12.32`**|**`< 2e-16 ***`**|
|**`poly(lstat, 5)3`**|**`-27.051`**|**`5.215`**|**`-5.19`**|**`3.1e-07 ***`**|
|**`poly(lstat, 5)4`**|**`25.452`**|**`5.215`**|**`4.88`**|**`1.4e-06 ***`**|
|**`poly(lstat, 5)5`**|**`-19.252`**|**`5.215`**|**`-3.69`**|**`0.00025 ***`**|
|`---`|||||
|`Signif.` **`codes`**`:`|`0 *** 0.`|`001 ** 0.01 `|`* 0.05 `|`. 0.1`<br>`1`|



```
Residualstandarderror:5.21on500degreesoffreedom
MultipleR-squared:0.682,AdjustedR-squared:0.679
F-statistic:214on5and500DF,p-value:<2e-16
```

Điều này cho thấy rằng việc bao gồm các thuật ngữ đa thức bổ sung, lên đến bậc năm, dẫn đến sự cải thiện trong sự phù hợp của mô hình (model fit)! Tuy nhiên, việc điều tra sâu hơn về dữ liệu cho thấy rằng không có thuật ngữ đa thức nào vượt quá bậc năm có giá trị _p_ (p-value) có ý nghĩa trong một hồi quy.

Theo mặc định, hàm `poly()` trực giao hóa (orthogonalizes) các biến dự báo: điều này có nghĩa là các đặc trưng (features) được xuất ra bởi hàm này không đơn giản là một chuỗi

3.6 Lab: Linear Regression 119 

lũy thừa của đối số. Tuy nhiên, một mô hình tuyến tính được áp dụng cho đầu ra của hàm `poly()` sẽ có cùng các giá trị khớp (fitted values) như một mô hình tuyến tính được áp dụng cho các đa thức thô (mặc dù các ước lượng hệ số, sai số chuẩn và giá trị p sẽ khác nhau). Để có được các đa thức thô từ hàm `poly()`, đối số `raw = TRUE` phải được sử dụng.

Tất nhiên, chúng ta không bị hạn chế trong việc sử dụng các phép biến đổi đa thức của các biến dự báo. Ở đây chúng ta thử một phép biến đổi logarit. <mark>`> summary(lm(medv`</mark> _<mark>∼</mark>_ <mark>`log(`</mark> **<mark>`rm`</mark>** <mark>`), data = Boston)) ...`</mark> 

### _3.6.6 Các biến dự báo định tính (Qualitative Predictors)_

Bây giờ chúng ta sẽ xem xét dữ liệu `Carseats`, là một phần của thư viện `ISLR2`. Chúng ta sẽ cố gắng dự đoán `Sales` (doanh số bán ghế ô tô trẻ em) ở 400 địa điểm dựa trên một số biến dự báo.

|`> head(Carse`<br>|`ats)`<br>||||||
|---|---|---|---|---|---|---|
|`Sales Comp`<br><br>|`Price `<br>|`Income `<br>|`Adverti`|`sing `<br>|`Population `<br>|`Price`<br>|
|`1`<br>`9.50`|`138`|`73`||`11`|`276`|`120`|
|`2 11.22`|`111`|`48`||`16`|`260`|`83`|
|`3 10.06`|`113`|`35`||`10`|`269`|`80`|
|`4`<br>`7.40`|`117`|`100`||`4`|`466`|`97`|
|`5`<br>`4.15`|`141`|`64`||`3`|`340`|`128`|
|`6 10.81`|`124`|`113`||`13`|`501`|`72`|
|`ShelveLoc `|`Age Ed`|`ucation `|`Urban`|`US`|||
|`1`<br>`Bad`|`42`|`17`|`Yes `|`Yes`|||
|`2`<br>`Good`|`65`|`10`|`Yes `|`Yes`|||
|`3`<br>`Medium`|`59`|`12`|`Yes `|`Yes`|||
|`4`<br>`Medium`|`55`|`14`|`Yes `|`Yes`|||
|`5`<br>`Bad`|`38`|`13`|`Yes`|`No`|||
|`6`<br>`Bad`|`78`|`16`|`No `|`Yes`|||



Dữ liệu `Carseats` bao gồm các biến dự báo định tính (qualitative predictors) chẳng hạn như `Shelveloc`, một chỉ báo về chất lượng của vị trí đặt kệ hàng—nghĩa là, không gian bên trong một cửa hàng nơi ghế ô tô được trưng bày—tại mỗi địa điểm. Biến dự báo `Shelveloc` có ba giá trị có thể: _Bad_, _Medium_, và _Good_. Với một biến định tính chẳng hạn như `Shelveloc`, `R` tự động tạo ra các biến giả (dummy variables). Dưới đây chúng ta khớp một mô hình hồi quy đa biến (multiple regression model) bao gồm một số thuật ngữ tương tác.

<mark>`>`</mark> **<mark>`lm`</mark>** <mark>`.fit <- lm(Sales`</mark> _<mark>∼</mark>_ <mark>`. + Income:Advertising + Price:Age, data = Carseats) > summary(`</mark> **<mark>`lm`</mark>** <mark>`.fit)`</mark> **<mark>`Call`</mark>** <mark>`:`</mark> **<mark>`lm`</mark>** <mark>`(`</mark> **<mark>`formula`</mark>** <mark>`= Sales`</mark> _<mark>∼</mark>_ <mark>`. + Income:Advertising + Price:Age, data = Carseats) Residuals: Min 1`</mark> **<mark>`Q`</mark>** <mark>`Median 3`</mark> **<mark>`Q`</mark>** <mark>`Max`</mark> 

120 3. Linear Regression 

```
-2.921-0.7500.0180.6753.341
```

|`Coefficients:`|`Estimate `|`Std. Error `|`t value `|`Pr(>|t|)`|
|---|---|---|---|---|
|`(Intercept)`|`6.575565`|`1.008747`|`6.52`|`2.2e-10 ***`|
|`CompPrice`|`0.092937`|`0.004118`|`22.57`|`< 2e-16 ***`|
|`Income`|`0.010894`|`0.002604`|`4.18`|`3.6e-05 ***`|
|`Advertising`|`0.070246`|`0.022609`|`3.11`|`0.00203 **`|
|`Population`|`0.000159`|`0.000368`|`0.43`|`0.66533`|
|`Price`|`-0.100806`|`0.007440`|`-13.55`|`< 2e-16 ***`|
|`ShelveLocGood`|`4.848676`|`0.152838`|`31.72`|`< 2e-16 ***`|
|`ShelveLocMedium`|`1.953262`|`0.125768`|`15.53`|`< 2e-16 ***`|
|`Age`|`-0.057947`|`0.015951`|`-3.63`|`0.00032 ***`|
|`Education`|`-0.020852`|`0.019613`|`-1.06`|`0.28836`|
|`UrbanYes`|`0.140160`|`0.112402`|`1.25`|`0.21317`|
|`USYes`|`-0.157557`|`0.148923`|`-1.06`|`0.29073`|
|`Income:Advertising`|`0.000751`|`0.000278`|`2.70`|`0.00729 **`|
|`Price:Age`<br>`---`|`0.000107`|`0.000133`|`0.80`|`0.42381`|
|`Signif.` **`codes`**`:`<br>`0 `|`*** 0.001 `|`** 0.01 * 0.`|`05 . 0.1`|`1`|



```
Residualstandarderror:1.01on386degreesoffreedom
MultipleR-squared:0.876,AdjustedR-squared:0.872
F-statistic:210on13and386DF,p-value:<2e-16
```

Hàm `contrasts()` trả về cách mã hóa mà `R` sử dụng cho các biến giả.

|`> attach(Carseats)`|
|---|
|`> contrasts(ShelveLoc)`|
|`Good Medium`|
|`Bad`<br>`0`<br>`0`|
|`Good`<br>`1`<br>`0`|
|`Medium`<br>`0`<br>`1`|



Sử dụng `?contrasts` để tìm hiểu về các cách mã hóa (contrasts) khác, và cách thiết lập chúng.

`R` đã tạo một biến giả `ShelveLocGood` nhận giá trị bằng 1 nếu vị trí kệ hàng là tốt (good), và 0 nếu ngược lại. Nó cũng đã tạo một biến giả `ShelveLocMedium` bằng 1 nếu vị trí kệ hàng là trung bình (medium), và 0 nếu ngược lại. Một vị trí kệ hàng xấu (bad) tương ứng với giá trị 0 cho mỗi trong hai biến giả. Việc hệ số cho `ShelveLocGood` trong đầu ra hồi quy là dương chỉ ra rằng một vị trí kệ hàng tốt có liên quan đến doanh số bán cao (so với một vị trí xấu). Và `ShelveLocMedium` có một hệ số dương nhỏ hơn, chỉ ra rằng một vị trí kệ hàng trung bình có liên quan đến doanh số bán cao hơn so với một vị trí kệ hàng xấu nhưng doanh số bán thấp hơn so với một vị trí kệ hàng tốt.

### _3.6.7 Viết các hàm (Writing Functions)_

Như chúng ta đã thấy, `R` đi kèm với nhiều hàm hữu ích, và thậm chí còn có nhiều hàm hơn khả dụng thông qua các thư viện `R`. Tuy nhiên, chúng ta sẽ thường xuyên

3.7 Exercises 121 

quan tâm đến việc thực hiện một thao tác mà không có hàm nào có sẵn. Trong trường hợp này, chúng ta có thể muốn tự viết hàm của riêng mình. Ví dụ, dưới đây chúng tôi cung cấp một hàm đơn giản để đọc các thư viện `ISLR2` và `MASS`, được gọi là `LoadLibraries()`. Trước khi chúng ta tạo hàm, `R` trả về một lỗi nếu chúng ta cố gọi nó.

###### <mark>`> LoadLibraries`</mark> 

```
Error:object`LoadLibraries 'notfound
>LoadLibraries()
Error:couldnotfindfunction"LoadLibraries"
```

Bây giờ chúng ta tạo hàm. Lưu ý rằng các ký hiệu `+` được in bởi `R` và không nên gõ vào. Ký hiệu `{` thông báo cho `R` rằng nhiều lệnh sắp được nhập vào. Nhấn _Enter_ sau khi gõ `{` sẽ khiến `R` in ký hiệu `+`. Sau đó, chúng ta có thể nhập bao nhiêu lệnh tùy thích, nhấn _Enter_ sau mỗi lệnh. Cuối cùng, ký hiệu `}` thông báo cho `R` rằng sẽ không có lệnh nào khác được nhập.

```
>LoadLibraries<-function(){
```

```
+library(ISLR2)
+library(MASS)
+print("Thelibrarieshavebeenloaded.")
+}
```

Bây giờ nếu chúng ta gõ vào `LoadLibraries`, `R` sẽ cho chúng ta biết những gì có trong hàm.

```
>LoadLibraries
```

```
function(){
library(ISLR2)
library(MASS)
print("Thelibrarieshavebeenloaded.")
}
```

Nếu chúng ta gọi hàm, các thư viện được tải vào và câu lệnh in (print statement) được xuất ra.

```
>LoadLibraries()
```

```
[1]"Thelibrarieshavebeenloaded."
```


## 3.7 Bài tập 

### _Lý thuyết_ 

1. Mô tả các giả thuyết vô hiệu mà các giá trị _p_ được đưa ra trong Bảng 3.4 tương ứng. Giải thích những kết luận bạn có thể rút ra dựa trên các giá trị _p_ này. Lời giải thích của bạn nên được diễn đạt theo khía cạnh `sales` , `TV` , `radio` , và `newspaper` , thay vì theo các hệ số của mô hình tuyến tính. 

2. Giải thích cẩn thận sự khác biệt giữa các phương pháp phân loại KNN và hồi quy KNN. 

122 3. Hồi quy tuyến tính 

3. Giả sử chúng ta có một tập dữ liệu với năm biến dự báo, _X_ 1 = GPA, _X_ 2 = IQ, _X_ 3 = Level (1 cho Đại học và 0 cho Trung học phổ thông), _X_ 4 = Tương tác giữa GPA và IQ, và _X_ 5 = Tương tác giữa GPA và Level. Biến phản hồi là mức lương khởi điểm sau khi tốt nghiệp (đơn vị hàng nghìn đô la). Giả sử chúng ta sử dụng bình phương tối thiểu để khớp mô hình, và nhận được _β_ 0 = 50 _, β_ 1 = 20 _, β_ 2 = 0 _._ 07 _, β_ 3 = 35 _, β_ 4 = 0 _._ 01 _, β_ 5 = _−_ 10. 

   - (a) Câu trả lời nào đúng, và tại sao? 

      - i. Đối với một giá trị cố định của IQ và GPA, trung bình những người tốt nghiệp trung học phổ thông kiếm được nhiều tiền hơn những người tốt nghiệp đại học. 

      - ii. Đối với một giá trị cố định của IQ và GPA, trung bình những người tốt nghiệp đại học kiếm được nhiều tiền hơn những người tốt nghiệp trung học phổ thông. 

      - iii. Đối với một giá trị cố định của IQ và GPA, trung bình những người tốt nghiệp trung học phổ thông kiếm được nhiều tiền hơn những người tốt nghiệp đại học, với điều kiện là GPA đủ cao. 

      - iv. Đối với một giá trị cố định của IQ và GPA, trung bình những người tốt nghiệp đại học kiếm được nhiều tiền hơn những người tốt nghiệp trung học phổ thông, với điều kiện là GPA đủ cao. 

   - (b) Dự báo mức lương của một người tốt nghiệp đại học với IQ là 110 và GPA là 4 _._ 0. 

   - (c) Đúng hay sai: Vì hệ số cho số hạng tương tác GPA/IQ rất nhỏ, có rất ít bằng chứng về hiệu ứng tương tác. Biện luận cho câu trả lời của bạn. 

4. Tôi thu thập một tập dữ liệu ( _n_ = 100 quan sát) chứa một biến dự báo duy nhất và một biến phản hồi định lượng. Sau đó tôi khớp một mô hình hồi quy tuyến tính với dữ liệu, cũng như một mô hình hồi quy bậc ba riêng biệt, tức là _Y_ = _β_ 0 + _β_ 1 _X_ + _β_ 2 _X_<sup>2</sup> + _β_ 3 _X_<sup>3</sup> + _ϵ_ . 

   - (a) Giả sử rằng mối quan hệ thực sự giữa X và Y là tuyến tính, tức là _Y_ = _β_ 0 + _β_ 1 _X_ + _ϵ_ . Xem xét tổng bình phương phần dư (RSS) huấn luyện cho hồi quy tuyến tính, và cả RSS huấn luyện cho hồi quy bậc ba. Chúng ta có kỳ vọng cái này thấp hơn cái kia, chúng ta có kỳ vọng chúng giống nhau, hay không có đủ thông tin để trả lời? Biện luận cho câu trả lời của bạn. 

   - (b) Trả lời (a) sử dụng RSS kiểm tra thay vì RSS huấn luyện. 

   - (c) Giả sử rằng mối quan hệ thực sự giữa X và Y không tuyến tính, nhưng chúng ta không biết nó khác tuyến tính bao xa. Xem xét RSS huấn luyện cho hồi quy tuyến tính, và cả RSS huấn luyện cho hồi quy bậc ba. Chúng ta có kỳ vọng cái này thấp hơn cái kia, chúng ta có kỳ vọng chúng giống nhau, hay không có đủ thông tin để trả lời? Biện luận cho câu trả lời của bạn. 

   - (d) Trả lời (c) sử dụng RSS kiểm tra thay vì RSS huấn luyện. 

3.7 Bài tập 

123 

5. Xem xét các giá trị được khớp là kết quả từ việc thực hiện hồi quy tuyến tính không có hệ số chặn. Trong thiết lập này, giá trị được khớp thứ _i_ có dạng 

trong đó 


![](images/chapter_3.pdf-0065-04.png)


Chứng minh rằng chúng ta có thể viết 


![](images/chapter_3.pdf-0065-06.png)


_ai′_ là gì? 

_Lưu ý: Chúng ta diễn giải kết quả này bằng cách nói rằng các giá trị được khớp từ hồi quy tuyến tính là_ tổ hợp tuyến tính _của các giá trị biến phản hồi._ 

6. Sử dụng (3.4), lập luận rằng trong trường hợp hồi quy tuyến tính đơn biến, đường bình phương tối thiểu luôn đi qua điểm (¯ _x,_ ¯ _y_ ). 

7. Trong văn bản có khẳng định rằng trong trường hợp hồi quy tuyến tính đơn biến của _Y_ theo _X_ , thống kê _R_<sup>2</sup> (3.17) bằng bình phương của độ tương quan giữa _X_ và _Y_ (3.18). Chứng minh rằng điều này là đúng. Để đơn giản, bạn có thể giả sử rằng _x_ ¯ = _y_ ¯ = 0. 


![](images/chapter_3.pdf-0065-11.png)


### _Thực hành_ 

8. Câu hỏi này liên quan đến việc sử dụng hồi quy tuyến tính đơn biến trên tập dữ liệu `Auto` . 

   - (a) Sử dụng hàm `lm()` để thực hiện một hồi quy tuyến tính đơn biến với `mpg` là biến phản hồi và `horsepower` là biến dự báo. Sử dụng hàm `summary()` để in kết quả. Nhận xét về đầu ra. Ví dụ: 

      - i. Có mối quan hệ nào giữa biến dự báo và biến phản hồi không? 

      - ii. Mối quan hệ giữa biến dự báo và biến phản hồi mạnh đến mức nào? 

      - iii. Mối quan hệ giữa biến dự báo và biến phản hồi là dương hay âm? 

      - iv. `mpg` được dự báo gắn liền với `horsepower` là 98 là bao nhiêu? Các khoảng tin cậy 95 % và khoảng dự báo tương ứng là gì? 

- 124 3. Hồi quy tuyến tính 

   - (b) Vẽ đồ thị biến phản hồi và biến dự báo. Sử dụng hàm `abline()` để hiển thị đường hồi quy bình phương tối thiểu. 

   - (c) Sử dụng hàm `plot()` để tạo ra các biểu đồ chẩn đoán của sự khớp hồi quy bình phương tối thiểu. Nhận xét về bất kỳ vấn đề nào bạn thấy với sự khớp này. 

9. Câu hỏi này liên quan đến việc sử dụng hồi quy tuyến tính đa biến trên tập dữ liệu `Auto` . 

   - (a) Tạo một ma trận biểu đồ phân tán bao gồm tất cả các biến trong tập dữ liệu. 

   - (b) Tính toán ma trận các độ tương quan giữa các biến bằng hàm `cor()` . Bạn sẽ cần loại trừ biến `name` , 

   - vốn là một biến định tính. 

   - (c) Sử dụng hàm `lm()` để thực hiện một hồi quy tuyến tính đa biến với `mpg` là biến phản hồi và tất cả các biến khác ngoại trừ `name` làm biến dự báo. Sử dụng hàm `summary()` để in kết quả. Nhận xét về đầu ra. Chẳng hạn: 

      - i. Có mối quan hệ nào giữa các biến dự báo và biến phản hồi không? 

      - ii. Những biến dự báo nào dường như có mối quan hệ có ý nghĩa thống kê với biến phản hồi? 

      - iii. Hệ số cho biến `year` gợi ý điều gì? 

   - (d) Sử dụng hàm `plot()` để tạo ra các biểu đồ chẩn đoán cho sự khớp hồi quy tuyến tính. Nhận xét về bất kỳ vấn đề nào bạn thấy với sự khớp này. Các biểu đồ phần dư có gợi ý bất kỳ điểm ngoại lai nào lớn bất thường không? Biểu đồ đòn bẩy có xác định được bất kỳ quan sát nào có đòn bẩy cao bất thường không? 

   - (e) Sử dụng các ký hiệu `*` và `:` để khớp các mô hình hồi quy tuyến tính với các hiệu ứng tương tác. Có bất kỳ sự tương tác nào dường như có ý nghĩa thống kê không? 

   - (f) Thử một vài phép biến đổi khác nhau của các biến, chẳng hạn như log( _X_ ), _√X_ , _X_<sup>2</sup> . Nhận xét về những phát hiện của bạn. 

10. Câu hỏi này nên được trả lời bằng cách sử dụng tập dữ liệu `Carseats` . 

   - (a) Khớp một mô hình hồi quy đa biến để dự báo `Sales` sử dụng `Price` , `Urban` , và `US` . 

   - (b) Cung cấp một diễn giải cho mỗi hệ số trong mô hình. Hãy cẩn thận—một số biến trong mô hình là định tính! 

   - (c) Viết mô hình dưới dạng phương trình, chú ý xử lý các biến định tính một cách thích hợp. 

3.7 Bài tập 125 

   - (d) Đối với những biến dự báo nào bạn có thể bác bỏ giả thuyết vô hiệu _H_ 0 : _βj_ = 0? 

   - (e) Trên cơ sở câu trả lời của bạn cho câu hỏi trước, hãy khớp một mô hình nhỏ hơn chỉ sử dụng các biến dự báo mà có bằng chứng về sự liên kết với kết quả. 

   - (f) Các mô hình trong (a) và (e) khớp với dữ liệu tốt như thế nào? (g) Sử dụng mô hình từ (e), lấy các khoảng tin cậy 95 % cho (các) hệ số. 

   - (h) Có bằng chứng về các điểm ngoại lai hoặc các quan sát có đòn bẩy cao trong mô hình từ (e) không? 

11. Trong bài toán này chúng ta sẽ khảo sát thống kê _t_ cho giả thuyết vô hiệu _H_ 0 : _β_ = 0 trong hồi quy tuyến tính đơn biến không có hệ số chặn. Để bắt đầu, chúng ta tạo ra một biến dự báo `x` và một biến phản hồi `y` như sau. 

```
>set.seed(1)
```

```
>x<-rnorm(100)
```

```
>y<-2*x+rnorm(100)
```

- (a) Thực hiện một hồi quy tuyến tính đơn biến của `y` theo `x` , _không có_ hệ số chặn. Báo cáo ước lượng hệ số _β_<sup>ˆ</sup> , sai số chuẩn của ước lượng hệ số này, và thống kê _t_ và giá trị _p_ gắn liền với giả thuyết vô hiệu _H_ 0 : _β_ = 0. Nhận xét về những kết quả này. (Bạn có thể thực hiện hồi quy không có hệ số chặn sử dụng lệnh `lm(y` _∼_ `x+0)` .) 

- (b) Bây giờ thực hiện một hồi quy tuyến tính đơn biến của `x` theo `y` không có hệ số chặn, và báo cáo ước lượng hệ số, sai số chuẩn của nó, và thống kê _t_ và các giá trị _p_ tương ứng gắn liền với giả thuyết vô hiệu _H_ 0 : _β_ = 0. Nhận xét về những kết quả này. 

- (c) Mối quan hệ giữa các kết quả thu được trong (a) và (b) là gì? 

- (d) Đối với hồi quy của _Y_ theo _X_ không có hệ số chặn, thống kê _t_ cho _H_ 0 : _β_ = 0 có dạng _β/_<sup>ˆ</sup> SE( _β_<sup>ˆ</sup> ), trong đó _β_<sup>ˆ</sup> được cho bởi (3.38), và trong đó 


![](images/chapter_3.pdf-0067-13.png)



![](images/chapter_3.pdf-0067-14.png)


(Các công thức này hơi khác so với các công thức được đưa ra trong Mục 3.1.1 và 3.1.2, vì ở đây chúng ta đang thực hiện hồi quy không có hệ số chặn.) Hãy chứng minh bằng đại số, và xác nhận bằng số liệu trong `R` , rằng thống kê _t_ có thể được viết thành 


![](images/chapter_3.pdf-0067-16.png)


- 126 3. Hồi quy tuyến tính 

   - (e) Sử dụng các kết quả từ (d), lập luận rằng thống kê _t_ cho hồi quy của `y` theo `x` là giống với thống kê _t_ cho hồi quy của `x` theo `y` . 

   - (f) Trong `R` , hãy chứng minh rằng khi hồi quy được thực hiện _có_ hệ số chặn, thống kê _t_ cho _H_ 0 : _β_ 1 = 0 là giống nhau cho hồi quy của `y` theo `x` và hồi quy của `x` theo `y` . 

12. Bài toán này liên quan đến hồi quy tuyến tính đơn biến không có hệ số chặn. 

   - (a) Nhắc lại rằng ước lượng hệ số _β_<sup>ˆ</sup> cho hồi quy tuyến tính của _Y_ theo _X_ không có hệ số chặn được cho bởi (3.38). Trong trường hợp nào ước lượng hệ số cho hồi quy của _X_ theo _Y_ giống với ước lượng hệ số cho hồi quy của _Y_ theo _X_ ? 

   - (b) Tạo một ví dụ trong `R` với _n_ = 100 quan sát trong đó ước lượng hệ số cho hồi quy của _X_ theo _Y_ là _khác với_ ước lượng hệ số cho hồi quy của _Y_ theo _X_ . 

   - (c) Tạo một ví dụ trong `R` với _n_ = 100 quan sát trong đó ước lượng hệ số cho hồi quy của _X_ theo _Y_ là _giống với_ ước lượng hệ số cho hồi quy của _Y_ theo _X_ . 

13. Trong bài tập này bạn sẽ tạo một số dữ liệu mô phỏng và sẽ khớp các mô hình hồi quy tuyến tính đơn biến với nó. Đảm bảo sử dụng `set.seed(1)` trước khi bắt đầu phần (a) để đảm bảo các kết quả nhất quán. 

   - (a) Sử dụng hàm `rnorm()` , tạo một vector, `x` , chứa 100 quan sát được rút ra từ phân phối _N_ (0 _,_ 1). Điều này đại diện cho một đặc trưng, _X_ . 

   - (b) Sử dụng hàm `rnorm()` , tạo một vector, `eps` , chứa 100 quan sát được rút ra từ phân phối _N_ (0 _,_ 0 _._ 25)—một phân phối chuẩn với trung bình bằng không và phương sai 0 _._ 25. 

   - (c) Sử dụng `x` và `eps` , tạo một vector `y` theo mô hình 


![](images/chapter_3.pdf-0068-11.png)


Chiều dài của vector `y` là bao nhiêu? Các giá trị của _β_ 0 và _β_ 1 trong mô hình tuyến tính này là gì? 

- (d) Tạo một biểu đồ phân tán hiển thị mối quan hệ giữa `x` và `y` . Nhận xét về những gì bạn quan sát được. 

- (e) Khớp một mô hình tuyến tính bình phương tối thiểu để dự báo `y` sử dụng `x` . Nhận xét về mô hình thu được. _β_<sup>ˆ</sup> 0 và _β_<sup>ˆ</sup> 1 so sánh như thế nào với _β_ 0 và _β_ 1? 

3.7 Bài tập 127 

   - (f) Hiển thị đường bình phương tối thiểu trên biểu đồ phân tán thu được ở (d). Vẽ đường hồi quy tổng thể trên biểu đồ, bằng một màu khác. Sử dụng lệnh `legend()` để tạo một chú giải phù hợp. 

   - (g) Bây giờ khớp một mô hình hồi quy đa thức dự báo `y` sử dụng `x` và x<sup>2</sup> . Có bằng chứng nào cho thấy số hạng bậc hai cải thiện sự khớp của mô hình không? Giải thích câu trả lời của bạn. 

   - (h) Lặp lại (a)–(f) sau khi sửa đổi quá trình tạo dữ liệu theo cách sao cho có _ít_ nhiễu hơn trong dữ liệu. Mô hình (3.39) vẫn phải giữ nguyên. Bạn có thể làm điều này bằng cách giảm phương sai của phân phối chuẩn được sử dụng để tạo ra số hạng sai số _ϵ_ trong (b). Mô tả các kết quả của bạn. 

   - (i) Lặp lại (a)–(f) sau khi sửa đổi quá trình tạo dữ liệu theo cách sao cho có _nhiều_ nhiễu hơn trong dữ liệu. Mô hình (3.39) vẫn phải giữ nguyên. Bạn có thể làm điều này bằng cách tăng phương sai của phân phối chuẩn được sử dụng để tạo ra số hạng sai số _ϵ_ trong (b). Mô tả các kết quả của bạn. 

   - (j) Các khoảng tin cậy cho _β_ 0 và _β_ 1 dựa trên tập dữ liệu gốc, tập dữ liệu nhiều nhiễu hơn, và tập dữ liệu ít nhiễu hơn là gì? Nhận xét về các kết quả của bạn. 

14. Bài toán này tập trung vào vấn đề _đa cộng tuyến_ . 

   - (a) Thực hiện các lệnh sau trong `R` : 

```
>set.seed(1)
>x1<-runif(100)
>x2<-0.5*x1+rnorm(100)/10
>y<-2+2*x1+0.3*x2+rnorm(100)
```

Dòng cuối cùng tương ứng với việc tạo một mô hình tuyến tính trong đó `y` là một hàm của `x1` và `x2` . Viết dạng của mô hình tuyến tính. Các hệ số hồi quy là gì? 

- (b) Độ tương quan giữa `x1` và `x2` là gì? Tạo một biểu đồ phân tán hiển thị mối quan hệ giữa các biến. 

- (c) Sử dụng dữ liệu này, khớp một hồi quy bình phương tối thiểu để dự báo `y` sử dụng `x1` và `x2` . Mô tả các kết quả thu được. _β_<sup>ˆ</sup> 0, _β_<sup>ˆ</sup> 1, và _β_<sup>ˆ</sup> 2 là gì? Chúng liên hệ như thế nào với _β_ 0, _β_ 1, và _β_ 2 thực sự? Bạn có thể bác bỏ giả thuyết vô hiệu _H_ 0 : _β_ 1 = 0 không? Còn giả thuyết vô hiệu _H_ 0 : _β_ 2 = 0 thì sao? 

- (d) Bây giờ khớp một hồi quy bình phương tối thiểu để dự báo `y` chỉ sử dụng `x1` . Nhận xét về các kết quả của bạn. Bạn có thể bác bỏ giả thuyết vô hiệu _H_ 0 : _β_ 1 = 0 không? 

- (e) Bây giờ khớp một hồi quy bình phương tối thiểu để dự báo `y` chỉ sử dụng `x2` . Nhận xét về các kết quả của bạn. Bạn có thể bác bỏ giả thuyết vô hiệu _H_ 0 : _β_ 1 = 0 không? 

- 128 3. Hồi quy tuyến tính 

   - (f) Các kết quả thu được trong (c)–(e) có mâu thuẫn với nhau không? Giải thích câu trả lời của bạn. 

   - (g) Bây giờ giả sử chúng ta thu được thêm một quan sát, mà không may bị đo sai. 

```
>x1<-c(x1,0.1)
>x2<-c(x2,0.8)
```

```
>y<-c(y,6)
```

Khớp lại các mô hình tuyến tính từ (c) đến (e) sử dụng dữ liệu mới này. Quan sát mới này có tác động gì đến mỗi mô hình? Trong mỗi mô hình, quan sát này có phải là một điểm ngoại lai không? Một điểm đòn bẩy cao không? Cả hai? Giải thích các câu trả lời của bạn. 

15. Bài toán này liên quan đến tập dữ liệu `Boston` , mà chúng ta đã thấy trong bài thực hành cho chương này. Bây giờ chúng ta sẽ cố gắng dự báo tỷ lệ tội phạm bình quân đầu người sử dụng các biến khác trong tập dữ liệu này. Nói cách khác, tỷ lệ tội phạm bình quân đầu người là biến phản hồi, và các biến khác là các biến dự báo. 

   - (a) Đối với mỗi biến dự báo, khớp một mô hình hồi quy tuyến tính đơn biến để dự báo biến phản hồi. Mô tả các kết quả của bạn. Trong những mô hình nào có một sự liên kết có ý nghĩa thống kê giữa biến dự báo và biến phản hồi? Tạo một số biểu đồ để chứng minh cho các khẳng định của bạn. 

   - (b) Khớp một mô hình hồi quy đa biến để dự báo biến phản hồi sử dụng tất cả các biến dự báo. Mô tả các kết quả của bạn. Đối với những biến dự báo nào chúng ta có thể bác bỏ giả thuyết vô hiệu _H_ 0 : _βj_ = 0? 

   - (c) Các kết quả của bạn từ (a) so sánh như thế nào với các kết quả của bạn từ (b)? Tạo một biểu đồ hiển thị các hệ số hồi quy đơn biến từ (a) trên trục _x_ , và các hệ số hồi quy đa biến từ (b) trên trục _y_ . Tức là, mỗi biến dự báo được hiển thị như một điểm duy nhất trong biểu đồ. Hệ số của nó trong một mô hình hồi quy tuyến tính đơn biến được hiển thị trên trục _x_ , và ước lượng hệ số của nó trong mô hình hồi quy tuyến tính đa biến được hiển thị trên trục _y_ . 

   - (d) Có bằng chứng về sự liên kết phi tuyến tính giữa bất kỳ biến dự báo nào và biến phản hồi không? Để trả lời câu hỏi này, đối với mỗi biến dự báo _X_ , khớp một mô hình có dạng 

      - _Y_ = _β_ 0 + _β_ 1 _X_ + _β_ 2 _X_<sup>2</sup> + _β_ 3 _X_<sup>3</sup> + _ϵ._ 


