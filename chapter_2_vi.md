2 

# Học Thống Kê 

## 2.1 Học Thống Kê Là Gì? 

Để tạo động lực cho việc nghiên cứu học thống kê, chúng ta bắt đầu với một ví dụ đơn giản. Giả sử chúng ta là các nhà tư vấn thống kê được một khách hàng thuê để điều tra mối liên hệ giữa quảng cáo và doanh số bán hàng của một sản phẩm cụ thể. Tập dữ liệu `Advertising` bao gồm doanh số (`sales`) của sản phẩm đó tại 200 thị trường khác nhau, cùng với ngân sách quảng cáo cho sản phẩm ở mỗi thị trường cho ba phương tiện truyền thông khác nhau: `TV`, `radio`, và báo chí (`newspaper`). Dữ liệu được hiển thị trong Hình 2.1. Khách hàng của chúng ta không thể trực tiếp tăng doanh số bán hàng của sản phẩm. Mặt khác, họ có thể kiểm soát chi tiêu quảng cáo trên từng phương tiện trong ba phương tiện truyền thông này. Do đó, nếu chúng ta xác định được có mối liên hệ giữa quảng cáo và doanh số, thì chúng ta có thể hướng dẫn khách hàng điều chỉnh ngân sách quảng cáo, qua đó gián tiếp làm tăng doanh số. Nói cách khác, mục tiêu của chúng ta là phát triển một mô hình chính xác có thể được sử dụng để dự đoán doanh số bán hàng dựa trên ngân sách của ba phương tiện truyền thông. 

Trong bối cảnh này, ngân sách quảng cáo là các *biến đầu vào* (input variables) trong khi `sales` là một *biến đầu ra* (output variable). Các biến đầu vào thường được ký hiệu bằng biến số $X$, với một chỉ số dưới để phân biệt chúng. Vì vậy, $X_1$ có thể là ngân sách `TV`, $X_2$ là ngân sách `radio`, và $X_3$ là ngân sách `newspaper`. Các biến đầu vào có nhiều tên gọi khác nhau, chẳng hạn như *biến dự báo* (predictors), *biến độc lập* (independent variables), *đặc trưng* (features), hay đôi khi chỉ gọi là *biến* (variables). Biến đầu ra—trong trường hợp này là `sales`—thường được gọi là *biến phản hồi* (response) hoặc *biến phụ thuộc* (dependent variable), và thường được ký hiệu bằng biến số $Y$. Trong suốt cuốn sách này, chúng tôi sẽ sử dụng các thuật ngữ này thay thế cho nhau.

16 2. Học Thống Kê 

![](images/chapter_2.pdf-0002-01.png)

**HÌNH 2.1.** *Tập dữ liệu* `Advertising` *. Biểu đồ hiển thị* `sales` * (hàng nghìn đơn vị) dưới dạng một hàm của ngân sách* `TV` *,* `radio` *và* `newspaper` * (hàng nghìn đô la), cho 200 thị trường khác nhau. Trong mỗi biểu đồ, chúng tôi thể hiện đường khớp bình phương tối thiểu đơn giản (simple least squares fit) của* `sales` *đối với biến đó, như được mô tả trong Chương 3. Nói cách khác, mỗi đường màu xanh lam đại diện cho một mô hình đơn giản có thể được sử dụng để dự đoán* `sales` *lần lượt từ* `TV` *,* `radio` *và* `newspaper` *.* 

Tổng quát hơn, giả sử chúng ta quan sát được một biến phản hồi định lượng $Y$ và $p$ biến dự báo khác nhau, $X_1, X_2, \dots, X_p$. Chúng ta giả định rằng có một mối quan hệ nào đó giữa $Y$ và $X = (X_1, X_2, \dots, X_p)$, có thể được viết dưới dạng rất tổng quát là

$$Y = f(X) + \epsilon$$

Ở đây $f$ là một hàm cố định nhưng chưa biết của $X_1, \dots, X_p$, và $\epsilon$ là một *số hạng sai số* (error term) ngẫu nhiên, độc lập với $X$ và có giá trị trung bình bằng 0. Trong công thức này, $f$ đại diện cho thông tin *có hệ thống* (systematic) mà $X$ cung cấp về $Y$.

Như một ví dụ khác, hãy xem xét bảng điều khiển bên trái của Hình 2.2, một biểu đồ thể hiện thu nhập (`income`) theo số năm học vấn (`years of education`) cho 30 cá nhân trong tập dữ liệu `Income`. Biểu đồ gợi ý rằng người ta có thể dự đoán `income` bằng cách sử dụng `years of education`. Tuy nhiên, hàm $f$ kết nối biến đầu vào với biến đầu ra nhìn chung là chưa biết. Trong tình huống này, người ta phải ước lượng $f$ dựa trên các điểm quan sát được. Vì `Income` là một tập dữ liệu mô phỏng, $f$ đã được biết và được thể hiện bằng đường cong màu xanh lam ở bảng điều khiển bên phải của Hình 2.2. Các đường dọc thể hiện các số hạng sai số $\epsilon$. Chúng ta lưu ý rằng một số trong 30 quan sát nằm phía trên đường cong màu xanh lam và một số nằm bên dưới nó; nhìn chung, các sai số có giá trị trung bình xấp xỉ bằng 0. 

Nhìn chung, hàm $f$ có thể liên quan đến nhiều hơn một biến đầu vào. Trong Hình 2.3, chúng tôi vẽ đồ thị `income` dưới dạng một hàm của `years of education` (số năm học vấn) và `seniority` (thâm niên). Ở đây $f$ là một bề mặt hai chiều phải được ước lượng dựa trên dữ liệu quan sát được.

38 2. Học Thống Kê 

![](images/chapter_2.pdf-0003-01.png)

**HÌNH 2.2.** *Tập dữ liệu* `Income` *.* Trái: *Các chấm màu đỏ là các giá trị quan sát được của* `income` * (hàng nghìn đô la) và* `years of education` *cho 30 cá nhân.* Phải: *Đường cong màu xanh lam đại diện cho mối quan hệ tiềm ẩn thực sự giữa* `income` *và* `years of education` *, điều mà nhìn chung là chưa biết (nhưng được biết trong trường hợp này vì dữ liệu đã được mô phỏng). Các đường màu đen thể hiện sai số liên quan đến mỗi quan sát. Lưu ý rằng một số sai số là dương (nếu một quan sát nằm trên đường cong màu xanh lam) và một số là âm (nếu một quan sát nằm dưới đường cong). Nhìn chung, các sai số này có giá trị trung bình xấp xỉ bằng 0.* 

Về bản chất, học thống kê đề cập đến một tập hợp các phương pháp tiếp cận để ước lượng $f$. Trong chương này, chúng tôi phác thảo một số khái niệm lý thuyết chính phát sinh trong việc ước lượng $f$, cũng như các công cụ để đánh giá các ước lượng thu được. 

### *2.1.1 Tại Sao Phải Ước Lượng $f$?* 

Có hai lý do chính mà chúng ta có thể muốn ước lượng $f$: *dự đoán* (prediction) và *suy luận* (inference). Chúng ta sẽ lần lượt thảo luận từng lý do.

#### Dự đoán 

Trong nhiều tình huống, một tập hợp các biến đầu vào $X$ có sẵn, nhưng khó có thể thu được biến đầu ra $Y$. Trong bối cảnh này, vì số hạng sai số có giá trị trung bình bằng 0, chúng ta có thể dự đoán $Y$ bằng cách sử dụng

$$\hat{Y} = \hat{f}(X)$$

trong đó $\hat{f}$ đại diện cho ước lượng của chúng ta cho $f$, và $\hat{Y}$ đại diện cho dự đoán kết quả cho $Y$. Trong bối cảnh này, $\hat{f}$ thường được coi như một *hộp đen* (black box), theo nghĩa là người ta thường không quan tâm đến dạng chính xác của $\hat{f}$, miễn là nó mang lại những dự đoán chính xác cho $Y$. 

Ví dụ, giả sử rằng $X_1, \dots, X_p$ là các đặc tính của mẫu máu của bệnh nhân có thể dễ dàng đo lường trong phòng thí nghiệm, và $Y$ là một biến mã hóa rủi ro của bệnh nhân đối với một phản ứng phụ nghiêm trọng với một loại thuốc cụ thể. 

18 2. Học Thống Kê 

![](images/chapter_2.pdf-0004-01.png)

**HÌNH 2.3.** *Biểu đồ hiển thị* `income` *dưới dạng một hàm của* `years of education` *và* `seniority` *trong tập dữ liệu* `Income` *. Bề mặt màu xanh lam đại diện cho mối quan hệ tiềm ẩn thực sự giữa* `income` *với* `years of education` *và* `seniority` *, điều này đã được biết vì dữ liệu được mô phỏng. Các chấm màu đỏ cho biết các giá trị quan sát được của các đại lượng này đối với 30 cá nhân.* 

Thật tự nhiên khi tìm cách dự đoán $Y$ bằng cách sử dụng $X$, vì khi đó chúng ta có thể tránh việc chỉ định loại thuốc nói trên cho những bệnh nhân có nguy cơ cao gặp phản ứng phụ — tức là, những bệnh nhân mà ước lượng của $Y$ ở mức cao. 

Độ chính xác của $\hat{Y}$ như một dự đoán cho $Y$ phụ thuộc vào hai đại lượng, mà chúng ta sẽ gọi là *sai số có thể giảm thiểu* (reducible error) và *sai số không thể giảm thiểu* (irreducible error). Nhìn chung, $\hat{f}$ sẽ không phải là một ước lượng hoàn hảo cho $f$, và sự thiếu chính xác này sẽ gây ra một số sai số. Sai số này là *có thể giảm thiểu* vì chúng ta có khả năng cải thiện độ chính xác của $\hat{f}$ bằng cách sử dụng kỹ thuật học thống kê phù hợp nhất để ước lượng $f$. Tuy nhiên, ngay cả khi có thể tạo ra một ước lượng hoàn hảo cho $f$, sao cho phản hồi ước lượng của chúng ta có dạng $\hat{Y} = f(X)$, thì dự đoán của chúng ta vẫn sẽ có một số sai số! Điều này là do $Y$ cũng là một hàm của $\epsilon$, mà theo định nghĩa, không thể được dự đoán bằng cách sử dụng $X$. Do đó, sự biến thiên liên quan đến $\epsilon$ cũng ảnh hưởng đến độ chính xác của các dự đoán của chúng ta. Điều này được gọi là sai số *không thể giảm thiểu*, bởi vì cho dù chúng ta có ước lượng $f$ tốt đến đâu, chúng ta cũng không thể làm giảm sai số do $\epsilon$ gây ra. 

Tại sao sai số không thể giảm thiểu lại lớn hơn 0? Đại lượng $\epsilon$ có thể chứa các biến chưa được đo lường nhưng lại hữu ích trong việc dự đoán $Y$: vì chúng ta không đo lường chúng, $f$ không thể sử dụng chúng cho dự đoán của mình. Đại lượng $\epsilon$ cũng có thể chứa sự biến thiên không thể đo lường được. Ví dụ, rủi ro xảy ra phản ứng phụ có thể thay đổi đối với một bệnh nhân nhất định vào một ngày nhất định, tùy thuộc vào sự thay đổi trong quá trình sản xuất của chính loại thuốc đó hoặc cảm giác khỏe mạnh nói chung của bệnh nhân vào ngày đó. 

2.1 Học Thống Kê Là Gì? 19 

Hãy xem xét một ước lượng cho trước $\hat{f}$ và một tập hợp các biến dự báo $X$, điều này mang lại dự đoán $\hat{Y} = \hat{f}(X)$. Tạm thời giả sử rằng cả $\hat{f}$ và $X$ đều cố định, sao cho sự biến thiên duy nhất đến từ $\epsilon$. Khi đó, có thể dễ dàng chứng minh được rằng

$$E(Y - \hat{Y})^2 = E[f(X) + \epsilon - \hat{f}(X)]^2 = [f(X) - \hat{f}(X)]^2 + \text{Var}(\epsilon)$$

trong đó $E(Y - \hat{Y})^2$ đại diện cho giá trị trung bình, hay *giá trị kỳ vọng* (expected value), của bình phương độ lệch giữa giá trị dự đoán và giá trị thực tế của $Y$, và $\text{Var}(\epsilon)$ đại diện cho *phương sai* (variance) liên quan đến số hạng sai số $\epsilon$. 

Trọng tâm của cuốn sách này là các kỹ thuật ước lượng $f$ với mục đích giảm thiểu sai số có thể giảm thiểu. Điều quan trọng cần ghi nhớ là sai số không thể giảm thiểu sẽ luôn tạo ra một giới hạn trên đối với độ chính xác của dự đoán của chúng ta về $Y$. Ranh giới này hầu như luôn luôn chưa được biết trong thực tế. 

#### Suy Luận 

Chúng ta thường quan tâm đến việc tìm hiểu mối liên hệ giữa $Y$ và $X_1, \dots, X_p$. Trong tình huống này, chúng ta muốn ước lượng $f$, nhưng mục tiêu của chúng ta không nhất thiết là đưa ra các dự đoán cho $Y$. Giờ đây $\hat{f}$ không thể được coi như một hộp đen, bởi vì chúng ta cần biết dạng chính xác của nó. Trong bối cảnh này, người ta có thể quan tâm đến việc trả lời các câu hỏi sau: 

- *Những biến dự báo nào có liên quan đến biến phản hồi?* Thường thì chỉ có một phần nhỏ các biến dự báo có sẵn là có liên quan đáng kể với $Y$. Việc xác định một vài biến dự báo *quan trọng* trong số một tập hợp lớn các biến có thể có là cực kỳ hữu ích, tùy thuộc vào ứng dụng. 

- *Mối quan hệ giữa biến phản hồi và mỗi biến dự báo là gì?* Một số biến dự báo có thể có mối quan hệ đồng biến với $Y$, theo nghĩa là các giá trị lớn hơn của biến dự báo có liên quan đến các giá trị lớn hơn của $Y$. Các biến dự báo khác có thể có mối quan hệ nghịch biến. Tùy thuộc vào độ phức tạp của $f$, mối quan hệ giữa biến phản hồi và một biến dự báo nhất định cũng có thể phụ thuộc vào giá trị của các biến dự báo khác. 

- *Mối quan hệ giữa $Y$ và mỗi biến dự báo có thể được tóm tắt một cách thỏa đáng bằng một phương trình tuyến tính, hay mối quan hệ đó phức tạp hơn?* Về mặt lịch sử, hầu hết các phương pháp ước lượng $f$ đều có dạng tuyến tính. Trong một số tình huống, giả định như vậy là hợp lý hoặc thậm chí mong muốn. Nhưng thường thì mối quan hệ thực sự phức tạp hơn, trong trường hợp đó một mô hình tuyến tính có thể không cung cấp một biểu diễn chính xác về mối quan hệ giữa các biến đầu vào và đầu ra. 

Trong cuốn sách này, chúng ta sẽ thấy một số ví dụ rơi vào bối cảnh dự đoán, bối cảnh suy luận, hoặc sự kết hợp của cả hai. 

20 2. Học Thống Kê 

Chẳng hạn, hãy xem xét một công ty đang quan tâm đến việc thực hiện một chiến dịch tiếp thị trực tiếp. Mục tiêu là xác định những cá nhân có khả năng phản hồi tích cực với thư gửi đi, dựa trên các quan sát về các biến nhân khẩu học được đo lường trên mỗi cá nhân. Trong trường hợp này, các biến nhân khẩu học đóng vai trò là các biến dự báo (predictors), và phản hồi đối với chiến dịch tiếp thị (tích cực hoặc tiêu cực) đóng vai trò là kết quả. Công ty không quan tâm đến việc có được sự hiểu biết sâu sắc về mối quan hệ giữa từng biến dự báo riêng lẻ và biến phản hồi; thay vào đó, công ty chỉ đơn giản muốn dự đoán chính xác biến phản hồi bằng cách sử dụng các biến dự báo. Đây là một ví dụ về lập mô hình cho mục đích dự đoán. 

Ngược lại, hãy xem xét dữ liệu `Advertising` được minh họa trong Hình 2.1. Người ta có thể quan tâm đến việc trả lời các câu hỏi như: 

- *Phương tiện truyền thông nào có liên quan đến doanh số bán hàng?* 

- *Phương tiện truyền thông nào tạo ra sự gia tăng lớn nhất cho doanh số bán hàng?* hoặc 

- *Mức tăng doanh số bán hàng lớn đến mức nào thì tương ứng với một mức tăng nhất định trong quảng cáo trên TV?* 

Tình huống này rơi vào hệ thống khái niệm suy luận (inference paradigm). Một ví dụ khác liên quan đến việc mô hình hóa thương hiệu của một sản phẩm mà khách hàng có thể mua dựa trên các biến số như giá cả, vị trí cửa hàng, mức chiết khấu, giá của đối thủ cạnh tranh, v.v. Trong tình huống này, người ta có thể thực sự quan tâm nhất đến mối liên hệ giữa mỗi biến số và xác suất mua hàng. Ví dụ, *mức độ liên quan giữa giá của sản phẩm với doanh số bán hàng là bao nhiêu?* Đây là một ví dụ về lập mô hình cho mục đích suy luận. 

Cuối cùng, một số mô hình hóa có thể được tiến hành cho cả dự đoán và suy luận. Ví dụ, trong bối cảnh bất động sản, người ta có thể tìm cách liên hệ giá trị của những ngôi nhà với các biến đầu vào như tỷ lệ tội phạm, quy hoạch vùng, khoảng cách đến một con sông, chất lượng không khí, trường học, mức thu nhập của cộng đồng, quy mô của những ngôi nhà, v.v. Trong trường hợp này, người ta có thể quan tâm đến mối liên hệ giữa mỗi biến đầu vào riêng lẻ và giá nhà — ví dụ, *một ngôi nhà sẽ có giá trị thêm bao nhiêu nếu nó có hướng nhìn ra sông?* Đây là một bài toán suy luận. Mặt khác, người ta có thể chỉ đơn giản quan tâm đến việc dự đoán giá trị của một ngôi nhà dựa trên các đặc điểm của nó: *ngôi nhà này đang bị định giá thấp hay định giá cao?* Đây là một bài toán dự đoán. 

Tùy thuộc vào mục tiêu cuối cùng của chúng ta là dự đoán, suy luận hay kết hợp cả hai, các phương pháp khác nhau để ước lượng $f$ có thể phù hợp. Ví dụ, các *mô hình tuyến tính* (linear models) cho phép thực hiện suy luận tương đối đơn giản và dễ diễn giải, nhưng có thể không mang lại các dự đoán chính xác như một số phương pháp khác. Ngược lại, một số phương pháp mang tính phi tuyến tính cao mà chúng ta thảo luận trong các chương sau của cuốn sách này có tiềm năng cung cấp các dự đoán khá chính xác cho $Y$, nhưng đổi lại là một mô hình kém diễn giải hơn mà ở đó việc suy luận trở nên khó khăn hơn. 

2.1 Học Thống Kê Là Gì? 21 

### *2.1.2 Chúng Ta Ước Lượng $f$ Bằng Cách Nào?* 

Xuyên suốt cuốn sách này, chúng ta khám phá nhiều phương pháp tuyến tính và phi tuyến tính để ước lượng $f$. Tuy nhiên, các phương pháp này thường có chung một số đặc điểm nhất định. Chúng tôi cung cấp một cái nhìn tổng quan về các đặc điểm chung này trong phần này. Chúng ta sẽ luôn giả định rằng chúng ta đã quan sát được một tập hợp gồm $n$ điểm dữ liệu khác nhau. Ví dụ trong Hình 2.2, chúng ta đã quan sát được $n = 30$ điểm dữ liệu. Các quan sát này được gọi là *dữ liệu huấn luyện* (training data) vì chúng ta sẽ sử dụng các quan sát huấn luyện này để huấn luyện, hoặc hướng dẫn cho phương pháp của chúng ta cách ước lượng $f$. Gọi $x_{ij}$ đại diện cho giá trị của biến dự báo, hoặc đầu vào, thứ $j$ cho quan sát thứ $i$, trong đó $i = 1, 2, \dots, n$ và $j = 1, 2, \dots, p$. Tương ứng, gọi $y_i$ đại diện cho biến phản hồi cho quan sát thứ $i$. Khi đó dữ liệu huấn luyện của chúng ta bao gồm $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$ trong đó $x_i = (x_{i1}, x_{i2}, \dots, x_{ip})^T$. 

Mục tiêu của chúng ta là áp dụng một phương pháp học thống kê vào dữ liệu huấn luyện nhằm ước lượng hàm chưa biết $f$. Nói cách khác, chúng chúng ta muốn tìm một hàm $\hat{f}$ sao cho $Y \approx \hat{f}(X)$ cho bất kỳ quan sát $(X, Y)$ nào. Nói rộng ra, hầu hết các phương pháp học thống kê cho nhiệm vụ này có thể được đặc trưng hóa thành dạng *có tham số* (parametric) hoặc *phi tham số* (non-parametric). Bây giờ chúng ta sẽ thảo luận ngắn gọn về hai loại phương pháp tiếp cận này. 

#### Các Phương Pháp Có Tham Số (Parametric Methods) 

Các phương pháp có tham số bao gồm một cách tiếp cận dựa trên mô hình gồm hai bước. 

1. Đầu tiên, chúng ta đưa ra một giả định về dạng hàm số, hoặc hình dạng của $f$. Ví dụ, một giả định rất đơn giản là $f$ tuyến tính theo $X$: 

$$f(X) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p$$

Đây là một *mô hình tuyến tính* (linear model), sẽ được thảo luận chi tiết trong Chương 3. Khi chúng ta đã giả định rằng $f$ là tuyến tính, bài toán ước lượng $f$ được đơn giản hóa đi rất nhiều. Thay vì phải ước lượng một hàm $p$ chiều $f(X)$ hoàn toàn tùy ý, người ta chỉ cần ước lượng $p + 1$ hệ số $\beta_0, \beta_1, \dots, \beta_p$. 

2. Sau khi một mô hình đã được chọn, chúng ta cần một quy trình sử dụng dữ liệu huấn luyện để *khớp* (fit) hoặc *huấn luyện* (train) mô hình đó. Trong trường hợp của mô hình tuyến tính 

(2.4), chúng ta cần ước lượng các tham số $\beta_0, \beta_1, \dots, \beta_p$. Tức là, chúng ta muốn tìm các giá trị của những tham số này sao cho 

$$Y \approx \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p$$

Cách tiếp cận phổ biến nhất để khớp mô hình (2.4) được gọi là *bình phương tối thiểu (thông thường)* (ordinary least squares), mà chúng ta sẽ thảo luận trong Chương 3. Tuy nhiên, bình phương tối thiểu chỉ là một trong nhiều cách có thể để khớp mô hình tuyến tính. Trong Chương 6, chúng ta sẽ thảo luận về các cách tiếp cận khác để ước lượng các tham số trong (2.4). 

22 2. Học Thống Kê 

![](images/chapter_2.pdf-0008-01.png)

**HÌNH 2.4.** *Một mô hình tuyến tính khớp bằng bình phương tối thiểu cho dữ liệu* `Income` *từ Hình 2.3. Các quan sát được hiển thị màu đỏ, và mặt phẳng màu vàng biểu thị phần khớp bình phương tối thiểu với dữ liệu.* 

Cách tiếp cận dựa trên mô hình vừa được mô tả được gọi là dạng *có tham số* (parametric); nó thu gọn bài toán ước lượng $f$ xuống thành bài toán ước lượng một tập hợp các tham số. Việc giả định dạng có tham số cho $f$ làm đơn giản hóa vấn đề ước lượng $f$ bởi vì nhìn chung sẽ dễ dàng hơn nhiều để ước lượng một tập hợp các tham số, chẳng hạn như $\beta_0, \beta_1, \dots, \beta_p$ trong mô hình tuyến tính (2.4), so với việc khớp một hàm $f$ hoàn toàn tùy ý. Nhược điểm tiềm tàng của cách tiếp cận có tham số là mô hình mà chúng ta chọn thường sẽ không khớp với dạng chưa biết thực sự của $f$. Nếu mô hình được chọn quá sai lệch so với $f$ thực sự, thì ước lượng của chúng ta sẽ kém chính xác. Chúng ta có thể cố gắng giải quyết vấn đề này bằng cách chọn những mô hình *linh hoạt* (flexible) có thể phù hợp với nhiều dạng hàm khác nhau đối với $f$. Nhưng nói chung, việc khớp một mô hình linh hoạt hơn đòi hỏi phải ước lượng một số lượng lớn hơn các tham số. Những mô hình phức tạp hơn này có thể dẫn đến một hiện tượng được gọi là *hiện tượng quá khớp* (overfitting) với dữ liệu, về cơ bản có nghĩa là chúng bám theo các sai số, hoặc *nhiễu* (noise), quá sát. Những vấn đề này sẽ được thảo luận xuyên suốt cuốn sách này. 

Hình 2.4 cho thấy một ví dụ về phương pháp tiếp cận có tham số được áp dụng cho dữ liệu `Income` từ Hình 2.3. Chúng ta đã khớp một mô hình tuyến tính có dạng 

$$ \text{income} \approx \beta_0 + \beta_1 \times \text{education} + \beta_2 \times \text{seniority} $$

Vì chúng ta đã giả định một mối quan hệ tuyến tính giữa biến phản hồi và hai biến dự báo, toàn bộ bài toán khớp đường cong thu gọn về việc ước lượng $\beta_0$, $\beta_1$, và $\beta_2$, điều mà chúng ta thực hiện bằng cách sử dụng hồi quy tuyến tính bình phương tối thiểu. So sánh Hình 2.3 với Hình 2.4, chúng ta có thể thấy rằng đường khớp tuyến tính được cho trong Hình 2.4 không hoàn toàn đúng: $f$ thực sự có một số độ cong mà đường khớp tuyến tính không nắm bắt được. Tuy nhiên, đường khớp tuyến tính dường như vẫn làm khá tốt việc nắm bắt 

2.1 Học Thống Kê Là Gì? 23 

![](images/chapter_2.pdf-0009-01.png)

**HÌNH 2.5.** *Một đường khớp spline màng mỏng mượt mà (smooth thin-plate spline) cho dữ liệu* `Income` *từ Hình 2.3 được hiển thị màu vàng; các quan sát được hiển thị màu đỏ. Các Spline được thảo luận trong Chương 7.* 

mối quan hệ đồng biến giữa `years of education` và `income`, cũng như mối quan hệ đồng biến nhưng yếu hơn một chút giữa `seniority` và `income`. Có thể là với một số lượng quan sát nhỏ như vậy, đây là cách tốt nhất mà chúng ta có thể làm. 

#### Các Phương Pháp Phi Tham Số (Non-Parametric Methods) 

Các phương pháp phi tham số không đưa ra các giả định rõ ràng về dạng hàm của $f$. Thay vào đó, chúng tìm kiếm một ước lượng của $f$ càng gần với các điểm dữ liệu càng tốt mà không bị quá thô ráp hoặc gợn sóng. Các phương pháp tiếp cận như vậy có thể có một lợi thế lớn so với các phương pháp tiếp cận có tham số: bằng cách tránh giả định về một dạng hàm cụ thể cho $f$, chúng có tiềm năng khớp chính xác với một phạm vi rộng hơn các hình dạng có thể có của $f$. Bất kỳ phương pháp tiếp cận có tham số nào cũng mang lại khả năng dạng hàm được sử dụng để ước lượng $f$ rất khác so với $f$ thực sự, trong trường hợp đó mô hình kết quả sẽ không khớp tốt với dữ liệu. Ngược lại, các phương pháp tiếp cận phi tham số hoàn toàn tránh được rủi ro này, vì về cơ bản không có giả định nào về dạng của $f$ được đưa ra. Nhưng các phương pháp tiếp cận phi tham số lại gặp phải một nhược điểm lớn: vì chúng không giảm bài toán ước lượng $f$ thành một số lượng nhỏ các tham số, nên cần một số lượng lớn các quan sát (nhiều hơn rất nhiều so với mức thường cần cho một phương pháp tiếp cận có tham số) để có thể thu được một ước lượng chính xác cho $f$. 

Một ví dụ về phương pháp tiếp cận phi tham số để khớp dữ liệu `Income` được hiển thị trong Hình 2.5. Một *spline màng mỏng* (thin-plate spline) được sử dụng để ước lượng $f$. Cách tiếp cận này không áp đặt bất kỳ mô hình được chỉ định trước nào lên $f$. Thay vào đó, nó cố gắng tạo ra một ước lượng cho $f$ càng sát với dữ liệu quan sát được càng tốt, với điều kiện là phần khớp — tức là, bề mặt màu vàng trong Hình 2.5 — phải 

24 2. Học Thống Kê 

![](images/chapter_2.pdf-0010-01.png)

**HÌNH 2.6.** *Một đường khớp spline màng mỏng thô ráp cho dữ liệu* `Income` *từ Hình 2.3. Đường khớp này có sai số bằng 0 trên dữ liệu huấn luyện.* 

*mượt mà* (smooth). Trong trường hợp này, phần khớp phi tham số đã tạo ra một ước lượng cực kỳ chính xác về $f$ thực sự được thể hiện trong Hình 2.3. Để khớp một spline màng mỏng, nhà phân tích dữ liệu phải chọn một mức độ mượt mà. Hình 2.6 cho thấy phần khớp spline màng mỏng tương tự sử dụng mức độ mượt mà thấp hơn, cho phép phần khớp trở nên thô ráp hơn. Ướ lượng thu được khớp hoàn hảo với dữ liệu quan sát được! Tuy nhiên, phần khớp spline được hiển thị trong Hình 2.6 biến động nhiều hơn đáng kể so với hàm thực sự $f$, từ Hình 2.3. Đây là một ví dụ về *hiện tượng quá khớp* (overfitting) với dữ liệu, điều mà chúng ta đã thảo luận trước đó. Đây là một tình huống không mong muốn vì phần khớp thu được sẽ không mang lại các ước lượng chính xác cho biến phản hồi trên những quan sát mới không nằm trong tập dữ liệu huấn luyện ban đầu. Chúng ta sẽ thảo luận về các phương pháp để chọn mức độ mượt mà *chính xác* trong Chương 5. Spline được thảo luận trong Chương 7. 

Như chúng ta đã thấy, có những ưu điểm và nhược điểm đối với các phương pháp có tham số và phi tham số trong học thống kê. Chúng ta sẽ khám phá cả hai loại phương pháp này trong suốt cuốn sách này. 

### *2.1.3 Sự Đánh Đổi Giữa Độ Chính Xác Của Dự Đoán Và Khả Năng Diễn Giải Mô Hình* 

Trong số nhiều phương pháp mà chúng ta xem xét trong cuốn sách này, một số ít linh hoạt hơn, hoặc bị gò bó hơn, theo nghĩa là chúng chỉ có thể tạo ra một phạm vi hình dạng tương đối nhỏ để ước lượng $f$. Ví dụ, hồi quy tuyến tính là một cách tiếp cận tương đối kém linh hoạt, bởi vì nó chỉ có thể tạo ra các hàm tuyến tính như các đường thẳng được hiển thị trong Hình 2.1 hoặc mặt phẳng được hiển thị trong Hình 2.4. Các phương pháp khác, chẳng hạn như spline màng mỏng được hiển thị trong Hình 2.5 và 2.6, 

2.1 Học Thống Kê Là Gì? 25 

![](images/chapter_2.pdf-0011-01.png)

**HÌNH 2.7.** *Biểu diễn sự đánh đổi giữa tính linh hoạt (flexibility) và khả năng diễn giải (interpretability), sử dụng các phương pháp học thống kê khác nhau. Nhìn chung, khi tính linh hoạt của một phương pháp tăng lên, thì khả năng diễn giải của nó giảm xuống.* 

linh hoạt hơn đáng kể vì chúng có thể tạo ra một phạm vi hình dạng có thể có rộng hơn nhiều để ước lượng $f$. 

Người ta có thể đặt ra câu hỏi hợp lý sau: *tại sao chúng ta lại chọn sử dụng một phương pháp gò bó hơn thay vì một cách tiếp cận rất linh hoạt?* Có một vài lý do giải thích cho việc chúng ta có thể thích một mô hình gò bó hơn. Nếu chúng ta chủ yếu quan tâm đến suy luận, thì các mô hình bị gò bó sẽ dễ diễn giải hơn nhiều. Chẳng hạn, khi mục tiêu là suy luận, mô hình tuyến tính có thể là một lựa chọn tốt vì sẽ khá dễ dàng để hiểu mối quan hệ giữa $Y$ và $X_1, X_2, \dots, X_p$. Ngược lại, các phương pháp tiếp cận rất linh hoạt, chẳng hạn như spline được thảo luận trong Chương 7 và được hiển thị trong Hình 2.5 và 2.6, cũng như các phương pháp boosting (tăng cường) được thảo luận trong Chương 8, có thể dẫn đến các ước lượng quá phức tạp đối với $f$ đến mức khó có thể hiểu được cách mỗi biến dự báo riêng lẻ liên kết với biến phản hồi như thế nào. 

Hình 2.7 cung cấp một minh họa về sự đánh đổi giữa tính linh hoạt và khả năng diễn giải cho một số phương pháp mà chúng ta đề cập trong cuốn sách này. Hồi quy tuyến tính bình phương tối thiểu, được thảo luận trong Chương 3, tương đối kém linh hoạt nhưng lại khá dễ diễn giải. Phương pháp *lasso*, được thảo luận trong Chương 6, dựa trên mô hình tuyến tính (2.4) nhưng sử dụng một quy trình khớp đường cong thay thế để ước lượng các hệ số $\beta_0, \beta_1, \dots, \beta_p$. Quy trình mới này gò bó hơn trong việc ước lượng các hệ số, và đặt một số hệ số trong số đó bằng đúng 0. Do đó, theo nghĩa này, lasso là một cách tiếp cận ít linh hoạt hơn so với hồi quy tuyến tính. Nó cũng dễ diễn giải hơn so với hồi quy tuyến tính, bởi vì trong mô hình cuối cùng, biến phản hồi sẽ chỉ liên quan đến một tập con nhỏ các biến dự báo — cụ thể là những biến có ước lượng hệ số khác 0. Các *mô hình cộng tính tổng quát* (Generalized additive models - GAMs), được thảo luận trong Chương 7, lại mở rộng mô hình tuyến tính (2.4) để cho phép một số mối quan hệ phi tuyến tính nhất định. Hậu quả là, 

26 2. Học Thống Kê 

GAM linh hoạt hơn hồi quy tuyến tính. Chúng cũng kém khả năng diễn giải hơn một chút so với hồi quy tuyến tính, vì mối quan hệ giữa mỗi biến dự báo và biến phản hồi hiện được mô phỏng bằng một đường cong. Cuối cùng, các phương pháp hoàn toàn phi tuyến tính như *bagging*, *boosting*, *máy học vector hỗ trợ* (support vector machines) với các kernel phi tuyến tính, và *mạng nơ-ron* (neural networks - học sâu), được thảo luận trong các Chương 8, 9, và 10, là những cách tiếp cận có tính linh hoạt cao nhưng lại khó diễn giải hơn. 

Chúng ta đã xác định được rằng khi suy luận là mục tiêu, có những lợi thế rõ ràng khi sử dụng các phương pháp học thống kê đơn giản và tương đối kém linh hoạt. Tuy nhiên, trong một số bối cảnh, chúng ta chỉ quan tâm đến dự đoán và khả năng diễn giải của mô hình dự báo không phải là điều được quan tâm đến. Ví dụ, nếu chúng ta tìm cách phát triển một thuật toán để dự đoán giá của một cổ phiếu, yêu cầu duy nhất của chúng ta đối với thuật toán đó là dự đoán chính xác — khả năng diễn giải không phải là mối bận tâm. Trong bối cảnh này, chúng ta có thể kỳ vọng rằng tốt nhất là sử dụng mô hình linh hoạt nhất hiện có. Thật đáng ngạc nhiên, điều này không phải lúc nào cũng đúng! Chúng ta sẽ thường thu được các dự đoán chính xác hơn khi sử dụng một phương pháp ít linh hoạt hơn. Hiện tượng này, thoạt nhìn có vẻ phản trực giác, lại liên quan đến tiềm năng xảy ra *hiện tượng quá khớp* (overfitting) trong các phương pháp có tính linh hoạt cao. Chúng ta đã thấy một ví dụ về hiện tượng quá khớp trong Hình 2.6. Chúng ta sẽ thảo luận về khái niệm rất quan trọng này sâu hơn trong Mục 2.2 và xuyên suốt cuốn sách này. 

### *2.1.4 Học Có Giám Sát Và Học Không Giám Sát* 

Hầu hết các bài toán học thống kê rơi vào một trong hai nhóm: *học có giám sát* (supervised) hoặc *học không giám sát* (unsupervised). Tất cả các ví dụ mà chúng ta đã thảo luận cho đến nay trong chương này đều thuộc lĩnh vực học có giám sát. Đối với mỗi quan sát của (các) biến dự báo $x_i$, $i = 1, \dots, n$, đều có một phép đo biến phản hồi liên quan $y_i$. Chúng ta mong muốn khớp một mô hình liên hệ biến phản hồi với các biến dự báo, với mục đích dự đoán chính xác biến phản hồi cho các quan sát trong tương lai (dự đoán) hoặc hiểu rõ hơn về mối quan hệ giữa biến phản hồi và các biến dự báo (suy luận). Nhiều phương pháp học thống kê cổ điển như hồi quy tuyến tính và *hồi quy logistic* (Chương 4), cũng như các cách tiếp cận hiện đại hơn như GAM, boosting, và máy học vector hỗ trợ, đều hoạt động trong lĩnh vực học có giám sát. Phần lớn nội dung cuốn sách này được dành cho bối cảnh này. 

Ngược lại, học không giám sát mô tả một tình huống có phần thách thức hơn, trong đó với mỗi quan sát $i = 1, \dots, n$, chúng ta quan sát được một vector các phép đo $x_i$ nhưng không có biến phản hồi liên quan $y_i$. Không thể khớp một mô hình hồi quy tuyến tính, vì không có biến phản hồi nào để dự đoán. Trong bối cảnh này, theo một nghĩa nào đó, chúng ta đang làm việc một cách mù quáng; tình huống này được gọi là *không giám sát* vì chúng ta thiếu một biến phản hồi có thể giám sát quá trình phân tích của chúng ta. Vậy loại phân tích thống kê nào là khả thi? Chúng ta có thể tìm hiểu các mối quan hệ giữa các biến số hoặc giữa các quan sát với nhau. Một công cụ học thống kê mà chúng ta có thể sử dụng 

2.1 Học Thống Kê Là Gì? 27 

![](images/chapter_2.pdf-0013-01.png)

**HÌNH 2.8.** *Một tập dữ liệu phân cụm bao gồm ba nhóm. Mỗi nhóm được hiển thị bằng một ký hiệu có màu sắc khác nhau.* Trái: *Ba nhóm được phân tách rõ ràng. Trong bối cảnh này, một phương pháp tiếp cận phân cụm có thể nhận diện thành công cả ba nhóm.* Phải: *Có một số sự chồng chéo giữa các nhóm. Giờ đây, nhiệm vụ phân cụm trở nên khó khăn hơn.* 

trong bối cảnh này là *phân tích cụm* (cluster analysis), hay phân cụm (clustering). Mục tiêu của phân tích cụm là xác định, dựa trên $x_1, \dots, x_n$, xem các quan sát có rơi vào các nhóm tương đối riêng biệt hay không. Ví dụ, trong một nghiên cứu phân khúc thị trường, chúng ta có thể quan sát nhiều đặc điểm (biến số) đối với các khách hàng tiềm năng, chẳng hạn như mã bưu điện, thu nhập gia đình và thói quen mua sắm. Chúng ta có thể tin rằng các khách hàng được chia thành các nhóm khác nhau, chẳng hạn như nhóm chi tiêu nhiều và nhóm chi tiêu ít. Nếu thông tin về mô hình chi tiêu của mỗi khách hàng có sẵn, thì một phân tích có giám sát sẽ khả thi. Tuy nhiên, thông tin này lại không có sẵn — tức là, chúng ta không biết liệu mỗi khách hàng tiềm năng có phải là người chi tiêu nhiều hay không. Trong bối cảnh này, chúng ta có thể cố gắng phân cụm khách hàng dựa trên các biến số đã được đo lường, nhằm xác định các nhóm khách hàng tiềm năng riêng biệt. Việc xác định các nhóm như vậy có thể mang lại nhiều điều thú vị bởi vì có thể các nhóm này sẽ khác nhau liên quan đến một số thuộc tính được quan tâm, chẳng hạn như thói quen chi tiêu. 

Hình 2.8 cung cấp một minh họa đơn giản về bài toán phân cụm. Chúng ta đã vẽ biểu đồ 150 quan sát với các phép đo trên hai biến số, $X_1$ và $X_2$. Mỗi quan sát tương ứng với một trong ba nhóm riêng biệt. Vì mục đích minh họa, chúng ta đã vẽ các thành viên của mỗi nhóm bằng các màu sắc và ký hiệu khác nhau. Tuy nhiên, trong thực tế các thành viên trong nhóm thường chưa được biết, và mục tiêu là xác định nhóm mà mỗi quan sát thuộc về. Trong bảng điều khiển bên trái của Hình 2.8, đây là một nhiệm vụ tương đối dễ dàng vì các nhóm được phân tách rõ ràng. Ngược lại, bảng điều khiển bên phải minh họa một bối cảnh nhiều thách thức hơn, trong đó có một số sự chồng chéo 

28 2. Học Thống Kê 

giữa các nhóm. Không thể kỳ vọng một phương pháp phân cụm phân bổ tất cả các điểm chồng chéo vào đúng nhóm của chúng (xanh lam, xanh lục hoặc cam). 

Trong các ví dụ được hiển thị ở Hình 2.8, chỉ có hai biến số, và vì vậy người ta có thể chỉ cần kiểm tra trực quan các biểu đồ phân tán của các quan sát để xác định các cụm. Tuy nhiên, trong thực tế, chúng ta thường gặp phải các tập dữ liệu chứa nhiều hơn hai biến số rất nhiều. Trong trường hợp này, chúng ta không thể dễ dàng vẽ biểu đồ cho các quan sát. Ví dụ, nếu có $p$ biến số trong tập dữ liệu của chúng ta, thì có thể tạo ra $p(p - 1)/2$ biểu đồ phân tán riêng biệt, và việc kiểm tra bằng mắt thường đơn giản không phải là một cách khả thi để xác định các cụm. Vì lý do này, các phương pháp phân cụm tự động là rất quan trọng. Chúng ta sẽ thảo luận về phân cụm và các phương pháp tiếp cận học không giám sát khác trong Chương 12. 

Nhiều bài toán rơi vào các hệ thống khái niệm học có giám sát hoặc học không giám sát một cách tự nhiên. Tuy nhiên, đôi khi câu hỏi liệu một phân tích nên được coi là có giám sát hay không giám sát lại kém rõ ràng hơn. Ví dụ, giả sử rằng chúng ta có một tập hợp gồm $n$ quan sát. Đối với $m$ quan sát, trong đó $m < n$, chúng ta có cả các phép đo cho biến dự báo và một phép đo cho biến phản hồi. Đối với $n - m$ quan sát còn lại, chúng ta có các phép đo biến dự báo nhưng không có phép đo biến phản hồi. Kịch bản như vậy có thể phát sinh nếu các biến dự báo có thể được đo lường với chi phí tương đối rẻ nhưng các biến phản hồi tương ứng lại tốn kém hơn nhiều để thu thập. Chúng ta gọi bối cảnh này là một bài toán *học bán giám sát* (semi-supervised learning). Trong bối cảnh này, chúng ta mong muốn sử dụng một phương pháp học thống kê có thể kết hợp $m$ quan sát có sẵn các phép đo biến phản hồi cũng như $n - m$ quan sát mà chúng ta chưa có. Mặc dù đây là một chủ đề thú vị, nhưng nó nằm ngoài phạm vi của cuốn sách này. 


### _2.1.5 Các bài toán Hồi quy so với Phân loại (Regression Versus Classification Problems)_ 

Các biến có thể được đặc trưng là biến _định lượng_ (quantitative) hoặc _định tính_ (qualitative - hay còn gọi là phân loại _categorical_). Các biến định lượng nhận các giá trị bằng số. Ví dụ như tuổi, chiều cao, hoặc thu nhập của một người, giá trị của một ngôi nhà, và giá của một cổ phiếu. Ngược lại, các biến định tính nhận các giá trị thuộc một trong $K$ _lớp_ (classes), hay phân loại khác nhau. Ví dụ về các biến định tính bao gồm tình trạng hôn nhân của một người (đã kết hôn hay chưa), thương hiệu của sản phẩm được mua (thương hiệu A, B hoặc C), liệu một người có vỡ nợ hay không (có hoặc không), hoặc chẩn đoán ung thư (Bệnh bạch cầu tủy cấp tính, Bệnh bạch cầu lympho cấp tính, hoặc Không mắc bệnh bạch cầu). Chúng ta có xu hướng gọi các bài toán có biến phản hồi định lượng là các bài toán _hồi quy_ (regression), trong khi những bài toán liên quan đến biến phản hồi định tính thường được gọi là các bài toán _phân loại_ (classification). Tuy nhiên, sự phân biệt này không phải lúc nào cũng rạch ròi. Hồi quy tuyến tính bình phương tối thiểu (Chương 3) được sử dụng với biến phản hồi định lượng, trong khi hồi quy logistic (Chương 4) thường được sử dụng với biến phản hồi định tính (hai lớp, hay _nhị phân_ - binary). Do đó, mặc dù có tên gọi như vậy, hồi quy logistic lại là một phương pháp phân loại. Nhưng vì nó ước lượng các xác suất của lớp, nó cũng có thể được coi như một phương pháp hồi quy. Một số phương pháp thống kê, chẳng hạn như $K$-láng giềng gần nhất (Chương 2 và 4) và boosting (Chương 8), có thể được sử dụng trong trường hợp biến phản hồi là định lượng hoặc định tính.

Chúng ta có xu hướng lựa chọn các phương pháp học thống kê dựa trên việc biến phản hồi là định lượng hay định tính; ví dụ, chúng ta có thể sử dụng hồi quy tuyến tính khi nó là định lượng và hồi quy logistic khi nó là định tính. Tuy nhiên, việc các _biến dự báo_ là định tính hay định lượng thường được coi là ít quan trọng hơn. Hầu hết các phương pháp học thống kê được thảo luận trong cuốn sách này đều có thể được áp dụng bất kể loại biến dự báo là gì, miễn là bất kỳ biến dự báo định tính nào cũng được _mã hóa_ (coded) đúng cách trước khi phân tích được thực hiện. Điều này được thảo luận trong Chương 3.

## 2.2 Đánh giá Độ chính xác của Mô hình (Assessing Model Accuracy)

Một trong những mục đích chính của cuốn sách này là giới thiệu cho người đọc một loạt các phương pháp học thống kê mở rộng vượt xa phương pháp hồi quy tuyến tính tiêu chuẩn. Tại sao cần phải giới thiệu quá nhiều phương pháp học thống kê khác nhau, thay vì chỉ một phương pháp _tốt nhất_? _Không có bữa trưa nào là miễn phí trong thống kê:_ không có một phương pháp nào vượt trội hơn tất cả các phương pháp khác trên mọi tập dữ liệu có thể có. Trên một tập dữ liệu cụ thể, một phương pháp cụ thể có thể hoạt động tốt nhất, nhưng một số phương pháp khác có thể hoạt động tốt hơn trên một tập dữ liệu tương tự nhưng khác biệt. Do đó, việc quyết định xem đối với bất kỳ tập dữ liệu cho trước nào thì phương pháp nào tạo ra kết quả tốt nhất là một nhiệm vụ quan trọng. Việc lựa chọn phương pháp tiếp cận tốt nhất có thể là một trong những phần khó khăn nhất của việc thực hiện học thống kê trong thực tế.

Trong phần này, chúng ta thảo luận về một số khái niệm quan trọng nhất phát sinh trong việc lựa chọn một quy trình học thống kê cho một tập dữ liệu cụ thể. Khi cuốn sách tiếp tục, chúng ta sẽ giải thích làm thế nào các khái niệm được trình bày ở đây có thể được áp dụng trong thực tế.

### _2.2.1 Đo lường Chất lượng Khớp (Measuring the Quality of Fit)_ 

Để đánh giá hiệu suất của một phương pháp học thống kê trên một tập dữ liệu cho trước, chúng ta cần một cách nào đó để đo lường xem các dự đoán của nó thực sự khớp với dữ liệu quan sát được tốt đến mức nào. Tức là, chúng ta cần định lượng mức độ mà giá trị biến phản hồi được dự đoán cho một quan sát nhất định gần với giá trị biến phản hồi thực sự cho quan sát đó. Trong thiết lập hồi quy, thước đo được sử dụng phổ biến nhất là _sai số toàn phương trung bình_ (mean squared error - MSE), được cho bởi

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{f}(x_i))^2 \quad (2.5)$$

trong đó $\hat{f}(x_i)$ là dự đoán mà $\hat{f}$ đưa ra cho quan sát thứ $i$. MSE sẽ nhỏ nếu các biến phản hồi được dự đoán rất gần với các biến phản hồi thực sự, và sẽ lớn nếu đối với một số quan sát, các biến phản hồi được dự đoán và thực sự khác biệt đáng kể.

MSE trong phương trình (2.5) được tính toán bằng cách sử dụng dữ liệu huấn luyện đã được sử dụng để khớp mô hình, và do đó nên được gọi chính xác hơn là _MSE huấn luyện_ (training MSE). Nhưng nhìn chung, chúng ta không thực sự quan tâm đến việc phương pháp này hoạt động tốt như thế nào trên dữ liệu huấn luyện. Thay vào đó, _chúng ta quan tâm đến độ chính xác của các dự đoán mà chúng ta thu được khi áp dụng phương pháp của mình vào dữ liệu kiểm tra chưa từng thấy trước đó_. Tại sao đây lại là điều chúng ta quan tâm? Giả sử rằng chúng ta quan tâm đến việc phát triển một thuật toán để dự đoán giá của một cổ phiếu dựa trên lợi nhuận cổ phiếu trước đó. Chúng ta có thể huấn luyện phương pháp này bằng cách sử dụng lợi nhuận cổ phiếu từ 6 tháng qua. Nhưng chúng ta không thực sự quan tâm phương pháp của mình dự đoán giá cổ phiếu của tuần trước tốt như thế nào. Thay vào đó, chúng ta quan tâm đến việc nó sẽ dự đoán giá của ngày mai hoặc giá của tháng tới tốt như thế nào. Tương tự như vậy, giả sử rằng chúng ta có các phép đo lâm sàng (ví dụ: cân nặng, huyết áp, chiều cao, tuổi, tiền sử gia đình mắc bệnh) đối với một số bệnh nhân, cũng như thông tin về việc mỗi bệnh nhân có mắc bệnh tiểu đường hay không. Chúng ta có thể sử dụng những bệnh nhân này để huấn luyện một phương pháp học thống kê nhằm dự đoán nguy cơ mắc bệnh tiểu đường dựa trên các phép đo lâm sàng. Trong thực tế, chúng ta muốn phương pháp này dự đoán chính xác nguy cơ mắc bệnh tiểu đường cho _những bệnh nhân trong tương lai_ dựa trên các phép đo lâm sàng của họ. Chúng ta không mấy quan tâm đến việc liệu phương pháp này có dự đoán chính xác nguy cơ mắc bệnh tiểu đường cho những bệnh nhân được sử dụng để huấn luyện mô hình hay không, vì chúng ta đã biết bệnh nhân nào trong số đó mắc bệnh tiểu đường.

Để trình bày một cách toán học hơn, giả sử rằng chúng ta khớp phương pháp học thống kê của mình trên các quan sát huấn luyện $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$, và chúng ta thu được ước lượng $\hat{f}$. Sau đó, chúng ta có thể tính $\hat{f}(x_1), \hat{f}(x_2), \dots, \hat{f}(x_n)$. Nếu những giá trị này xấp xỉ bằng $y_1, y_2, \dots, y_n$, thì MSE huấn luyện được cho bởi (2.5) là nhỏ. Tuy nhiên, chúng ta thực sự không quan tâm đến việc liệu $\hat{f}(x_i) \approx y_i$; thay vào đó, chúng ta muốn biết liệu $\hat{f}(x_0)$ có xấp xỉ bằng $y_0$ hay không, trong đó $(x_0, y_0)$ là một _quan sát kiểm tra chưa từng thấy trước đó, không được sử dụng để huấn luyện phương pháp học thống kê_. Chúng ta muốn chọn phương pháp mang lại _MSE kiểm tra_ (test MSE) thấp nhất, trái ngược với MSE huấn luyện thấp nhất. Nói cách khác, nếu chúng ta có một số lượng lớn các quan sát kiểm tra, chúng ta có thể tính

$$Ave(y_0 - \hat{f}(x_0))^2 \quad (2.6)$$

trung bình bình phương sai số dự đoán cho các quan sát kiểm tra $(x_0, y_0)$ này. Chúng ta muốn chọn mô hình có đại lượng này càng nhỏ càng tốt. Làm thế nào chúng ta có thể cố gắng chọn một phương pháp làm giảm thiểu MSE kiểm tra? Trong một số trường hợp, chúng ta có thể có sẵn một tập dữ liệu kiểm tra—nghĩa là chúng ta có thể có quyền truy cập vào một tập hợp các quan sát không được sử dụng để huấn luyện phương pháp học thống kê. Khi đó, chúng ta chỉ cần đánh giá (2.6) trên các quan sát kiểm tra và chọn phương pháp học có MSE kiểm tra là nhỏ nhất. Nhưng nếu không có các quan sát kiểm tra thì sao? Trong trường hợp đó, người ta có thể tưởng tượng ra việc chỉ chọn một phương pháp học thống kê giúp giảm thiểu MSE huấn luyện (2.5). Điều này có vẻ như là một cách tiếp cận hợp lý, vì MSE huấn luyện và MSE kiểm tra có vẻ liên quan chặt chẽ với nhau.

![](images/chapter_2.pdf-0017-01.png)

**HÌNH 2.9.** Trái: _Dữ liệu được mô phỏng từ $f$, được hiển thị bằng màu đen. Ba ước lượng của $f$ được hiển thị: đường hồi quy tuyến tính (đường màu cam), và hai đường khớp spline làm trơn (các đường màu xanh lam và xanh lục)._ Phải: _MSE huấn luyện (đường màu xám), MSE kiểm tra (đường màu đỏ), và MSE kiểm tra tối thiểu có thể trên tất cả các phương pháp (đường đứt nét). Các hình vuông đại diện cho MSE huấn luyện và MSE kiểm tra cho ba đường khớp được hiển thị ở bảng bên trái._

Đáng tiếc là có một vấn đề cơ bản với chiến lược này: không có gì đảm bảo rằng phương pháp có MSE huấn luyện thấp nhất cũng sẽ có MSE kiểm tra thấp nhất. Nói một cách khái quát, vấn đề là nhiều phương pháp thống kê ước lượng cụ thể các hệ số nhằm giảm thiểu MSE của tập huấn luyện. Đối với các phương pháp này, MSE của tập huấn luyện có thể khá nhỏ, nhưng MSE kiểm tra thường lớn hơn nhiều.

Hình 2.9 minh họa hiện tượng này trên một ví dụ đơn giản. Trong bảng bên trái của Hình 2.9, chúng ta đã tạo ra các quan sát từ (2.1) với hàm $f$ thực sự được cho bởi đường cong màu đen. Các đường cong màu cam, xanh lam và xanh lục minh họa ba ước lượng có thể có cho $f$ thu được bằng cách sử dụng các phương pháp với mức độ linh hoạt tăng dần. Đường màu cam là đường khớp hồi quy tuyến tính, tương đối kém linh hoạt. Các đường cong màu xanh lam và xanh lục được tạo ra bằng cách sử dụng _spline làm trơn_ (smoothing splines), được thảo luận trong Chương 7, với các mức độ độ trơn khác nhau. Rõ ràng là khi mức độ linh hoạt tăng lên, các đường cong khớp với dữ liệu quan sát chặt chẽ hơn. Đường cong màu xanh lục linh hoạt nhất và khớp với dữ liệu rất tốt; tuy nhiên, chúng ta quan sát thấy rằng nó khớp với hàm $f$ thực (được hiển thị bằng màu đen) kém vì nó quá ngoằn ngoèo. Bằng cách điều chỉnh mức độ linh hoạt của đường khớp spline làm trơn, chúng ta có thể tạo ra nhiều đường khớp khác nhau cho dữ liệu này.

Bây giờ chúng ta chuyển sang bảng bên phải của Hình 2.9. Đường cong màu xám hiển thị MSE huấn luyện trung bình như một hàm của độ linh hoạt, hoặc chính thức hơn là _bậc tự do_ (degrees of freedom), cho một số spline làm trơn. Bậc tự do là một đại lượng tóm tắt tính linh hoạt của một đường cong; nó được thảo luận đầy đủ hơn trong Chương 7. Các hình vuông màu cam, xanh lam và xanh lục biểu thị các MSE liên quan đến các đường cong tương ứng trong bảng bên trái. Một đường cong bị hạn chế hơn và do đó trơn tru hơn có ít bậc tự do hơn một đường cong ngoằn ngoèo—lưu ý rằng trong Hình 2.9, hồi quy tuyến tính ở đầu hạn chế nhất, với hai bậc tự do. MSE huấn luyện giảm đơn điệu khi tính linh hoạt tăng lên. Trong ví dụ này hàm $f$ thực sự là phi tuyến tính, và do đó đường khớp tuyến tính màu cam không đủ linh hoạt để ước lượng tốt hàm $f$. Đường cong màu xanh lục có MSE huấn luyện thấp nhất trong cả ba phương pháp, vì nó tương ứng với đường cong linh hoạt nhất trong ba đường cong được khớp ở bảng bên trái.

Trong ví dụ này, chúng ta biết hàm thực $f$, và do đó chúng ta cũng có thể tính toán MSE kiểm tra trên một tập kiểm tra rất lớn, như một hàm của tính linh hoạt. (Tất nhiên, nói chung $f$ là chưa biết, vì vậy điều này sẽ không khả thi.) MSE kiểm tra được hiển thị bằng đường cong màu đỏ ở bảng bên phải của Hình 2.9. Giống như MSE huấn luyện, MSE kiểm tra ban đầu giảm khi mức độ linh hoạt tăng lên. Tuy nhiên, tại một số điểm, MSE kiểm tra chững lại và sau đó bắt đầu tăng trở lại. Do đó, cả hai đường cong màu cam và xanh lục đều có MSE kiểm tra cao. Đường cong màu xanh lam làm giảm thiểu MSE kiểm tra, điều này không có gì đáng ngạc nhiên vì về mặt trực quan, nó dường như ước lượng hàm $f$ tốt nhất ở bảng bên trái của Hình 2.9. Đường đứt nét nằm ngang chỉ ra $Var(\epsilon)$, phần sai số không thể giảm thiểu được trong (2.3), tương ứng với MSE kiểm tra đạt được thấp nhất trong tất cả các phương pháp có thể có. Do đó, spline làm trơn được biểu diễn bằng đường cong màu xanh lam gần với mức tối ưu.

Trong bảng bên phải của Hình 2.9, khi tính linh hoạt của phương pháp học thống kê tăng lên, chúng ta quan sát thấy sự giảm đơn điệu trong MSE huấn luyện và hình dáng chữ U (_U-shape_) trong MSE kiểm tra. Đây là đặc tính cơ bản của học thống kê, đúng với mọi tập dữ liệu đang có và bất kể phương pháp thống kê nào đang được sử dụng. Khi độ linh hoạt của mô hình tăng, MSE huấn luyện sẽ giảm, nhưng MSE kiểm tra có thể không giảm. Khi một phương pháp nhất định mang lại MSE huấn luyện nhỏ nhưng MSE kiểm tra lớn, chúng ta được cho là đang làm cho dữ liệu có _hiện tượng quá khớp_ (overfitting). Điều này xảy ra do quy trình học thống kê của chúng ta đang hoạt động quá mức để tìm kiếm các mẫu trong dữ liệu huấn luyện, và có thể đang thu nhận một số mẫu chỉ do sự tình cờ ngẫu nhiên gây ra thay vì do các thuộc tính thực sự của hàm chưa biết $f$. Khi chúng ta gặp hiện tượng quá khớp với dữ liệu huấn luyện, MSE kiểm tra sẽ rất lớn vì các mẫu giả định mà phương pháp tìm thấy trong dữ liệu huấn luyện đơn giản là không tồn tại trong dữ liệu kiểm tra. Lưu ý rằng bất kể hiện tượng quá khớp có xảy ra hay không, chúng ta gần như luôn mong đợi MSE huấn luyện nhỏ hơn MSE kiểm tra vì hầu hết các phương pháp học thống kê trực tiếp hoặc gián tiếp tìm cách làm giảm thiểu MSE huấn luyện. Hiện tượng quá khớp đề cập cụ thể đến trường hợp trong đó một mô hình ít linh hoạt hơn sẽ mang lại MSE kiểm tra nhỏ hơn.

Hình 2.10 cung cấp một ví dụ khác trong đó hàm thực $f$ xấp xỉ tuyến tính. Một lần nữa, chúng ta quan sát thấy rằng MSE huấn luyện giảm đơn điệu khi độ linh hoạt của mô hình tăng lên và có hình dáng chữ U trong MSE kiểm tra. Tuy nhiên, vì hàm thực gần với tuyến tính, MSE kiểm tra chỉ giảm nhẹ trước khi tăng trở lại, do đó đường khớp bình phương tối thiểu màu cam tốt hơn đáng kể so với đường cong màu xanh lục có tính linh hoạt cao.

![](images/chapter_2.pdf-0019-01.png)

**HÌNH 2.10.** _Các chi tiết giống như trong Hình 2.9, sử dụng một hàm $f$ thực khác rất gần với tuyến tính. Trong bối cảnh này, hồi quy tuyến tính cung cấp một đường khớp rất tốt với dữ liệu._

Cuối cùng, Hình 2.11 hiển thị một ví dụ trong đó hàm $f$ có tính phi tuyến tính cao. Các đường cong MSE huấn luyện và kiểm tra vẫn thể hiện cùng các mẫu chung, nhưng bây giờ có sự giảm nhanh trong cả hai đường cong trước khi MSE kiểm tra bắt đầu tăng chậm.

Trong thực tế, người ta thường có thể tính MSE huấn luyện tương đối dễ dàng, nhưng việc ước lượng MSE kiểm tra khó khăn hơn đáng kể vì thông thường không có sẵn dữ liệu kiểm tra. Như ba ví dụ trước minh họa, mức độ linh hoạt tương ứng với mô hình có MSE kiểm tra tối thiểu có thể thay đổi đáng kể giữa các tập dữ liệu. Xuyên suốt cuốn sách này, chúng ta thảo luận về nhiều phương pháp tiếp cận có thể được sử dụng trong thực tế để ước lượng điểm tối thiểu này. Một phương pháp quan trọng là _kiểm chứng chéo_ (cross-validation) (Chương 5), là một phương pháp để ước lượng MSE kiểm tra bằng cách sử dụng dữ liệu huấn luyện.

### _2.2.2 Sự Đánh đổi giữa Độ chệch và Phương sai (The Bias-Variance Trade-Off)_ 

Hình dáng chữ U được quan sát thấy trong các đường cong MSE kiểm tra (Hình 2.9–2.11) hóa ra là kết quả của hai đặc tính cạnh tranh nhau của các phương pháp học thống kê. Mặc dù chứng minh toán học nằm ngoài phạm vi của cuốn sách này, nhưng có thể chỉ ra rằng kỳ vọng MSE kiểm tra, đối với một giá trị cho trước $x_0$, luôn có thể được phân tích thành tổng của ba đại lượng cơ bản: _phương sai_ (variance) của $\hat{f}(x_0)$, bình phương _độ chệch_ (bias) của $\hat{f}(x_0)$ và phương sai của các số hạng sai số $\epsilon$. Tức là,

![](images/chapter_2.pdf-0020-01.png)

**HÌNH 2.11.** _Các chi tiết giống như trong Hình 2.9, sử dụng một hàm $f$ khác khác xa với tuyến tính. Trong bối cảnh này, hồi quy tuyến tính cung cấp một đường khớp rất kém với dữ liệu._

$$E(y_0 - \hat{f}(x_0))^2 = Var(\hat{f}(x_0)) + [Bias(\hat{f}(x_0))]^2 + Var(\epsilon) \quad (2.7)$$

Ở đây, ký hiệu $E(y_0 - \hat{f}(x_0))^2$ định nghĩa _kỳ vọng MSE kiểm tra_ tại $x_0$, và đề cập đến MSE kiểm tra trung bình mà chúng ta sẽ thu được nếu chúng ta liên tục ước lượng $f$ bằng cách sử dụng một số lượng lớn các tập huấn luyện, và kiểm tra từng tập tại $x_0$. Kỳ vọng MSE kiểm tra tổng thể có thể được tính bằng cách lấy trung bình $E(y_0 - \hat{f}(x_0))^2$ trên tất cả các giá trị có thể có của $x_0$ trong tập kiểm tra. Phương trình 2.7 cho chúng ta biết rằng để giảm thiểu kỳ vọng sai số kiểm tra, chúng ta cần chọn một phương pháp học thống kê đồng thời đạt được _phương sai thấp_ và _độ chệch thấp_. Lưu ý rằng phương sai vốn dĩ là một đại lượng không âm, và bình phương độ chệch cũng không âm. Do đó, chúng ta thấy rằng kỳ vọng MSE kiểm tra không bao giờ có thể nằm dưới $Var(\epsilon)$, phần sai số không thể giảm thiểu được từ (2.3).

Chúng ta hiểu thế nào là _phương sai_ và _độ chệch_ của một phương pháp học thống kê? _Phương sai_ đề cập đến lượng mà $\hat{f}$ sẽ thay đổi nếu chúng ta ước lượng nó bằng cách sử dụng một tập dữ liệu huấn luyện khác. Vì dữ liệu huấn luyện được sử dụng để khớp phương pháp học thống kê, nên các tập dữ liệu huấn luyện khác nhau sẽ dẫn đến một $\hat{f}$ khác nhau. Nhưng lý tưởng nhất là ước lượng cho $f$ không nên thay đổi quá nhiều giữa các tập huấn luyện. Tuy nhiên, nếu một phương pháp có phương sai cao thì những thay đổi nhỏ trong dữ liệu huấn luyện có thể dẫn đến những thay đổi lớn trong $\hat{f}$. Nhìn chung, các phương pháp thống kê linh hoạt hơn có phương sai cao hơn. Hãy xem xét các đường cong màu xanh lục và màu cam trong Hình 2.9. Đường cong màu xanh lục linh hoạt đang bám theo các quan sát rất chặt chẽ. Nó có phương sai cao vì việc thay đổi bất kỳ điểm dữ liệu nào trong số này cũng có thể khiến ước lượng $\hat{f}$ thay đổi đáng kể. Ngược lại, đường thẳng bình phương tối thiểu màu cam tương đối kém linh hoạt và có phương sai thấp, vì việc di chuyển bất kỳ một quan sát nào cũng có khả năng chỉ gây ra sự dịch chuyển nhỏ ở vị trí của đường thẳng.

Mặt khác, _độ chệch_ đề cập đến sai số được đưa ra do việc xấp xỉ một bài toán thực tế, vốn có thể cực kỳ phức tạp, bằng một mô hình đơn giản hơn nhiều. Ví dụ, hồi quy tuyến tính giả định rằng có một mối quan hệ tuyến tính giữa $Y$ và $X_1, X_2, \dots, X_p$. Rất khó có khả năng bất kỳ vấn đề thực tế nào lại thực sự có một mối quan hệ tuyến tính đơn giản như vậy, và do đó, việc thực hiện hồi quy tuyến tính chắc chắn sẽ dẫn đến một số độ chệch nhất định trong ước lượng của $f$. Trong Hình 2.11, hàm thực $f$ về cơ bản là phi tuyến, vì vậy cho dù chúng ta có bao nhiêu quan sát huấn luyện đi chăng nữa, sẽ không thể tạo ra một ước lượng chính xác bằng cách sử dụng hồi quy tuyến tính. Nói cách khác, hồi quy tuyến tính dẫn đến độ chệch cao trong ví dụ này. Tuy nhiên, trong Hình 2.10 hàm thực $f$ rất gần với tuyến tính, và do đó nếu có đủ dữ liệu, hồi quy tuyến tính sẽ có khả năng tạo ra một ước lượng chính xác. Nhìn chung, các phương pháp linh hoạt hơn dẫn đến ít độ chệch hơn.

Theo quy luật chung, khi chúng ta sử dụng các phương pháp linh hoạt hơn, phương sai sẽ tăng và độ chệch sẽ giảm. Tốc độ thay đổi tương đối của hai đại lượng này quyết định liệu MSE kiểm tra sẽ tăng hay giảm. Khi chúng ta tăng tính linh hoạt của một lớp các phương pháp, độ chệch ban đầu có xu hướng giảm nhanh hơn so với mức tăng của phương sai. Do đó, kỳ vọng MSE kiểm tra giảm xuống. Tuy nhiên, ở một điểm nào đó, việc tăng độ linh hoạt ít tác động đến độ chệch nhưng lại bắt đầu làm tăng đáng kể phương sai. Khi điều này xảy ra, MSE kiểm tra sẽ tăng lên. Lưu ý rằng chúng ta đã quan sát thấy mô hình giảm MSE kiểm tra này sau đó là tăng MSE kiểm tra ở các bảng bên phải của Hình 2.9–2.11.

Ba biểu đồ trong Hình 2.12 minh họa Phương trình 2.7 cho các ví dụ trong Hình 2.9–2.11. Trong mỗi trường hợp, đường cong liền nét màu xanh lam biểu diễn bình phương độ chệch, cho các mức độ linh hoạt khác nhau, trong khi đường cong màu cam tương ứng với phương sai. Đường đứt nét nằm ngang biểu diễn $Var(\epsilon)$, phần sai số không thể giảm thiểu được. Cuối cùng, đường cong màu đỏ, tương ứng với MSE của tập kiểm tra, là tổng của ba đại lượng này. Trong cả ba trường hợp, phương sai tăng và độ chệch giảm khi tính linh hoạt của phương pháp tăng. Tuy nhiên, mức độ linh hoạt tương ứng với MSE kiểm tra tối ưu khác nhau đáng kể giữa ba tập dữ liệu, vì bình phương độ chệch và phương sai thay đổi ở các tốc độ khác nhau trong mỗi tập dữ liệu. Trong bảng bên trái của Hình 2.12, độ chệch ban đầu giảm nhanh, dẫn đến sự giảm mạnh ban đầu của kỳ vọng MSE kiểm tra. Mặt khác, trong bảng ở giữa của Hình 2.12 hàm thực $f$ gần với tuyến tính, vì vậy chỉ có sự giảm nhỏ về độ chệch khi độ linh hoạt tăng, và MSE kiểm tra chỉ giảm nhẹ trước khi tăng nhanh khi phương sai tăng. Cuối cùng, ở bảng bên phải của Hình 2.12, khi độ linh hoạt tăng lên, có sự giảm mạnh về độ chệch vì hàm thực $f$ mang tính phi tuyến rất cao. Cũng có rất ít sự gia tăng về phương sai khi độ linh hoạt tăng. Do đó, MSE kiểm tra giảm đáng kể trước khi trải qua một sự gia tăng nhỏ do tính linh hoạt của mô hình tăng lên.

![](images/chapter_2.pdf-0022-01.png)

**HÌNH 2.12.** _Bình phương độ chệch (đường màu xanh lam), phương sai (đường màu cam), $Var(\epsilon)$ (đường đứt nét), và MSE kiểm tra (đường màu đỏ) đối với ba tập dữ liệu trong Hình 2.9–2.11. Đường chấm thẳng đứng chỉ ra mức độ linh hoạt tương ứng với MSE kiểm tra nhỏ nhất._

Mối quan hệ giữa độ chệch, phương sai, và MSE của tập kiểm tra được đưa ra trong Phương trình 2.7 và được hiển thị trong Hình 2.12 được gọi là _sự đánh đổi giữa độ chệch và phương sai_ (bias-variance trade-off). Hiệu suất tốt trên tập kiểm tra của một phương pháp học thống kê đòi hỏi phương sai thấp cũng như bình phương độ chệch thấp. Sự việc này được gọi là một sự đánh đổi vì rất dễ để có được một phương pháp có độ chệch cực thấp nhưng phương sai cao (ví dụ, bằng cách vẽ một đường cong đi qua mọi quan sát huấn luyện) hoặc một phương pháp có phương sai rất thấp nhưng độ chệch cao (bằng cách khớp một đường thẳng nằm ngang với dữ liệu). Thách thức nằm ở việc tìm ra một phương pháp mà cả phương sai và bình phương độ chệch đều thấp. Sự đánh đổi này là một trong những chủ đề lặp lại quan trọng nhất trong cuốn sách này.

Trong một tình huống thực tế mà $f$ không được quan sát thấy, nhìn chung không thể tính toán rõ ràng MSE kiểm tra, độ chệch, hoặc phương sai cho một phương pháp học thống kê. Tuy nhiên, người ta nên luôn ghi nhớ sự đánh đổi giữa độ chệch và phương sai. Trong cuốn sách này, chúng ta khám phá các phương pháp cực kỳ linh hoạt và do đó về cơ bản có thể loại bỏ độ chệch. Tuy nhiên, điều này không đảm bảo rằng chúng sẽ vượt trội hơn một phương pháp đơn giản hơn nhiều như hồi quy tuyến tính. Lấy một ví dụ cực đoan, giả sử rằng hàm thực $f$ là tuyến tính. Trong tình huống này, hồi quy tuyến tính sẽ không có độ chệch, khiến cho một phương pháp linh hoạt hơn rất khó cạnh tranh. Ngược lại, nếu hàm thực $f$ mang tính phi tuyến cao và chúng ta có một số lượng lớn các quan sát huấn luyện, thì chúng ta có thể làm tốt hơn bằng cách sử dụng một cách tiếp cận mang tính linh hoạt cao, như trong Hình 2.11. Trong Chương 5, chúng ta thảo luận về kiểm chứng chéo, đây là một cách để ước lượng MSE kiểm tra bằng cách sử dụng dữ liệu huấn luyện.

### _2.2.3 Thiết lập Phân loại (The Classification Setting)_ 

Cho đến nay, cuộc thảo luận của chúng ta về độ chính xác của mô hình đã tập trung vào thiết lập hồi quy. Nhưng nhiều khái niệm mà chúng ta đã gặp, chẳng hạn như sự đánh đổi giữa độ chệch và phương sai, chuyển sang thiết lập phân loại với chỉ một số sửa đổi do thực tế là $y_i$ không còn là định lượng nữa. Giả sử rằng chúng ta tìm cách ước lượng $f$ trên cơ sở các quan sát huấn luyện $\{(x_1, y_1), \dots, (x_n, y_n)\}$, trong đó bây giờ $y_1, \dots, y_n$ là định tính. Cách tiếp cận phổ biến nhất để định lượng độ chính xác của ước lượng $\hat{f}$ của chúng ta là _tỷ lệ sai số huấn luyện_ (training error rate), tỷ lệ những sai sót được tạo ra nếu chúng ta áp dụng ước lượng $\hat{f}$ của mình cho các quan sát huấn luyện:

$$\frac{1}{n} \sum_{i=1}^{n} I(y_i \neq \hat{y}_i) \quad (2.8)$$

Ở đây $\hat{y}_i$ là nhãn lớp được dự đoán cho quan sát thứ $i$ bằng cách sử dụng $\hat{f}$. Và $I(y_i \neq \hat{y}_i)$ là một _biến chỉ báo_ (indicator variable) bằng 1 nếu $y_i \neq \hat{y}_i$ và bằng 0 nếu $y_i = \hat{y}_i$. Nếu $I(y_i \neq \hat{y}_i) = 0$ thì quan sát thứ $i$ đã được phân loại chính xác bởi phương pháp phân loại của chúng ta; mặt khác nó đã bị phân loại sai. Do đó Phương trình 2.8 tính tỷ lệ phân loại sai.

Phương trình 2.8 được gọi là tỷ lệ sai số huấn luyện vì nó được tính toán dựa trên dữ liệu đã được sử dụng để huấn luyện bộ phân loại của chúng ta. Giống như trong thiết lập hồi quy, chúng quan tâm nhất đến tỷ lệ sai số có được từ việc áp dụng bộ phân loại của mình cho các quan sát kiểm tra không được sử dụng trong quá trình huấn luyện. _Tỷ lệ sai số kiểm tra_ (test error rate) liên quan đến một tập hợp các quan sát kiểm tra có dạng $(x_0, y_0)$ được cho bởi

$$Ave(I(y_0 \neq \hat{y}_0)) \quad (2.9)$$

trong đó $\hat{y}_0$ là nhãn lớp được dự đoán có được từ việc áp dụng bộ phân loại cho quan sát kiểm tra có biến dự báo $x_0$. Một bộ phân loại _tốt_ là bộ phân loại mà sai số kiểm tra (2.9) là nhỏ nhất.

**Bộ phân loại Bayes (The Bayes Classifier)**

Có thể chỉ ra (mặc dù bằng chứng nằm ngoài phạm vi của cuốn sách này) rằng tỷ lệ sai số kiểm tra cho trong (2.9) trung bình được tối thiểu hóa bằng một bộ phân loại rất đơn giản giúp _gán từng quan sát cho lớp có khả năng nhất, khi biết các giá trị biến dự báo của nó_. Nói cách khác, chúng ta chỉ cần gán một quan sát kiểm tra với vectơ biến dự báo $x_0$ cho lớp $j$ sao cho

$$Pr(Y = j | X = x_0) \quad (2.10)$$

là lớn nhất. Lưu ý rằng (2.10) là một _xác suất có điều kiện_ (conditional probability): nó là xác suất mà $Y = j$, khi biết vectơ biến dự báo quan sát được $x_0$. Bộ phân loại rất đơn giản này được gọi là _bộ phân loại Bayes_. Trong một bài toán hai lớp trong đó chỉ có hai giá trị biến phản hồi có thể có, giả sử _lớp 1_ hoặc _lớp 2_, bộ phân loại Bayes tương ứng với việc dự đoán lớp một nếu $Pr(Y = 1 | X = x_0) > 0.5$, và lớp hai trong trường hợp còn lại.

![](images/chapter_2.pdf-0024-01.png)

**HÌNH 2.13.** _Một tập dữ liệu mô phỏng bao gồm 100 quan sát trong mỗi một trong hai nhóm, được chỉ báo bằng màu xanh lam và màu cam. Đường đứt nét màu tím đại diện cho ranh giới quyết định Bayes. Lưới nền màu cam chỉ ra khu vực trong đó một quan sát kiểm tra sẽ được gán cho lớp màu cam, và lưới nền màu xanh lam chỉ ra khu vực trong đó một quan sát kiểm tra sẽ được gán cho lớp màu xanh lam._

Hình 2.13 cung cấp một ví dụ sử dụng một tập dữ liệu mô phỏng trong không gian hai chiều bao gồm các biến dự báo $X_1$ và $X_2$. Các vòng tròn màu cam và màu xanh lam tương ứng với các quan sát huấn luyện thuộc về hai lớp khác nhau. Đối với mỗi giá trị của $X_1$ và $X_2$, có một xác suất khác nhau của việc biến phản hồi là màu cam hay màu xanh lam. Vì đây là dữ liệu mô phỏng, chúng ta biết dữ liệu được tạo ra như thế nào và chúng ta có thể tính toán xác suất có điều kiện cho mỗi giá trị của $X_1$ và $X_2$. Khu vực bóng mờ màu cam phản ánh tập hợp các điểm có $Pr(Y = \text{cam} | X)$ lớn hơn 50%, trong khi khu vực bóng mờ màu xanh lam chỉ ra tập hợp các điểm có xác suất dưới 50%. Đường đứt nét màu tím biểu diễn các điểm mà tại đó xác suất bằng đúng 50%. Đây được gọi là _ranh giới quyết định Bayes_ (Bayes decision boundary). Dự đoán của bộ phân loại Bayes được xác định bởi ranh giới quyết định Bayes; một quan sát rơi vào phía màu cam của ranh giới sẽ được gán cho lớp màu cam, và tương tự một quan sát nằm bên phía màu xanh lam của ranh giới sẽ được gán cho lớp màu xanh lam.

Bộ phân loại Bayes tạo ra tỷ lệ sai số kiểm tra thấp nhất có thể, được gọi là _tỷ lệ sai số Bayes_ (Bayes error rate). Vì bộ phân loại Bayes sẽ luôn chọn lớp mà (2.10) là lớn nhất, nên tỷ lệ sai số tại $X = x_0$ sẽ là $1 - \max_j Pr(Y = j | X = x_0)$. Nhìn chung, tỷ lệ sai số Bayes tổng thể được cho bởi

$$1 - E\left(\max_j Pr(Y=j | X)\right) \quad (2.11)$$

trong đó kỳ vọng tính trung bình xác suất trên tất cả các giá trị có thể có của $X$. Đối với dữ liệu mô phỏng của chúng ta, tỷ lệ sai số Bayes là 0.133. Nó lớn hơn 0, vì các lớp trùng lặp trong quần thể thực, điều này ngụ ý rằng $\max_j Pr(Y = j | X = x_0) < 1$ đối với một số giá trị của $x_0$. Tỷ lệ sai số Bayes tương tự như phần sai số không thể giảm thiểu được, đã thảo luận ở phần trước.

**$K$-Láng giềng Gần nhất ($K$-Nearest Neighbors)**

Về lý thuyết, chúng ta luôn muốn dự đoán các biến phản hồi định tính bằng cách sử dụng bộ phân loại Bayes. Nhưng đối với dữ liệu thực, chúng ta không biết phân phối có điều kiện của $Y$ khi biết $X$, và do đó việc tính toán bộ phân loại Bayes là không thể. Do đó, bộ phân loại Bayes đóng vai trò như một tiêu chuẩn vàng không thể đạt được mà để so sánh các phương pháp khác với nó. Nhiều phương pháp tiếp cận cố gắng ước lượng phân phối có điều kiện của $Y$ khi biết $X$, và sau đó phân loại một quan sát nhất định vào lớp có xác suất _ước lượng_ cao nhất. Một phương pháp như vậy là bộ phân loại _$K$-láng giềng gần nhất_ ($K$-nearest neighbors - KNN). Cho trước một số nguyên dương $K$ và một quan sát kiểm tra $x_0$, bộ phân loại KNN trước tiên xác định $K$ điểm trong dữ liệu huấn luyện gần nhất với $x_0$, được biểu diễn bằng $\mathcal{N}_0$. Sau đó nó ước lượng xác suất có điều kiện cho lớp $j$ bằng tỷ lệ các điểm trong $\mathcal{N}_0$ mà có giá trị biến phản hồi bằng $j$:

$$Pr(Y = j | X = x_0) = \frac{1}{K} \sum_{i \in \mathcal{N}_0} I(y_i = j) \quad (2.12)$$

Cuối cùng, KNN phân loại quan sát kiểm tra $x_0$ vào lớp có xác suất lớn nhất từ (2.12).

Hình 2.14 cung cấp một ví dụ minh họa của cách tiếp cận KNN. Trong bảng bên trái, chúng ta đã vẽ một tập dữ liệu huấn luyện nhỏ bao gồm sáu quan sát màu xanh lam và sáu quan sát màu cam. Mục tiêu của chúng ta là đưa ra dự đoán cho điểm được đánh dấu bằng dấu chữ thập đen. Giả sử rằng chúng ta chọn $K = 3$. Khi đó KNN trước tiên sẽ xác định ba quan sát gần với dấu chữ thập nhất. Vùng lân cận này được hiển thị dưới dạng một vòng tròn. Nó bao gồm hai điểm màu xanh lam và một điểm màu cam, dẫn đến các xác suất ước lượng là 2/3 cho lớp màu xanh lam và 1/3 cho lớp màu cam. Do đó KNN sẽ dự đoán rằng dấu chữ thập đen thuộc về lớp màu xanh lam. Trong bảng bên phải của Hình 2.14, chúng ta đã áp dụng cách tiếp cận KNN với $K = 3$ tại tất cả các giá trị có thể có cho $X_1$ và $X_2$, và đã vẽ vào ranh giới quyết định KNN tương ứng.

Mặc dù thực tế nó là một phương pháp tiếp cận rất đơn giản, nhưng KNN thường có thể tạo ra các bộ phân loại gần một cách đáng ngạc nhiên với bộ phân loại Bayes tối ưu. Hình 2.15 hiển thị ranh giới quyết định KNN, sử dụng $K = 10$, khi được áp dụng cho tập dữ liệu mô phỏng lớn hơn từ Hình 2.13. Lưu ý rằng mặc dù phân phối thực sự không được bộ phân loại KNN biết đến, ranh giới quyết định KNN rất gần với ranh giới của bộ phân loại Bayes. Tỷ lệ sai số kiểm tra khi sử dụng KNN là 0.1363, gần với tỷ lệ sai số Bayes là 0.1304.

![](images/chapter_2.pdf-0026-01.png)

**HÌNH 2.14.** _Phương pháp tiếp cận KNN, sử dụng $K = 3$, được minh họa trong một tình huống đơn giản với sáu quan sát màu xanh lam và sáu quan sát màu cam._ Trái: _một quan sát kiểm tra tại đó nhãn lớp được dự đoán mong muốn được hiển thị dưới dạng dấu chữ thập đen. Ba điểm gần nhất với quan sát kiểm tra được xác định, và người ta dự đoán rằng quan sát kiểm tra thuộc về lớp xuất hiện phổ biến nhất, trong trường hợp này là màu xanh lam._ Phải: _Ranh giới quyết định KNN cho ví dụ này được hiển thị bằng màu đen. Lưới nền màu xanh lam chỉ ra khu vực mà một quan sát kiểm tra sẽ được gán cho lớp màu xanh lam, và lưới màu cam chỉ ra khu vực mà nó sẽ được gán cho lớp màu cam._

![](images/chapter_2.pdf-0026-04.png)

**HÌNH 2.15.** _Đường cong màu đen chỉ ra ranh giới quyết định KNN trên dữ liệu từ Hình 2.13, sử dụng $K = 10$. Ranh giới quyết định Bayes được hiển thị dưới dạng đường đứt nét màu tím. Ranh giới quyết định KNN và Bayes rất giống nhau._

![](images/chapter_2.pdf-0027-01.png)

**HÌNH 2.16.** _Một sự so sánh các ranh giới quyết định KNN (đường liền nét màu đen) thu được bằng cách sử dụng $K = 1$ và $K = 100$ trên dữ liệu từ Hình 2.13. Với $K = 1$, ranh giới quyết định quá linh hoạt, trong khi với $K = 100$ nó không đủ linh hoạt. Ranh giới quyết định Bayes được hiển thị dưới dạng đường đứt nét màu tím._

Sự lựa chọn $K$ có tác động mạnh mẽ đến bộ phân loại KNN thu được. Hình 2.16 hiển thị hai đường khớp KNN cho dữ liệu mô phỏng từ Hình 2.13, sử dụng $K = 1$ và $K = 100$. Khi $K = 1$, ranh giới quyết định quá linh hoạt và tìm thấy các mẫu trong dữ liệu không tương ứng với ranh giới quyết định Bayes. Điều này tương ứng với một bộ phân loại có độ chệch thấp nhưng phương sai rất cao. Khi $K$ lớn hơn, phương pháp trở nên kém linh hoạt hơn và tạo ra một ranh giới quyết định gần với tuyến tính. Điều này tương ứng với bộ phân loại có phương sai thấp nhưng độ chệch cao. Trên tập dữ liệu mô phỏng này, cả $K = 1$ và $K = 100$ đều không đưa ra dự đoán tốt: chúng có tỷ lệ sai số kiểm tra lần lượt là 0.1695 và 0.1925.

Cũng giống như trong thiết lập hồi quy, không có mối quan hệ mạnh mẽ giữa tỷ lệ sai số huấn luyện và tỷ lệ sai số kiểm tra. Với $K = 1$, tỷ lệ sai số huấn luyện KNN là 0, nhưng tỷ lệ sai số kiểm tra có thể khá cao. Nói chung, khi chúng ta sử dụng các phương pháp phân loại linh hoạt hơn, tỷ lệ sai số huấn luyện sẽ giảm nhưng tỷ lệ sai số kiểm tra có thể không giảm. Trong Hình 2.17, chúng ta đã vẽ sơ đồ sai số kiểm tra và huấn luyện KNN như một hàm của $1/K$. Khi $1/K$ tăng lên, phương pháp trở nên linh hoạt hơn. Giống như trong thiết lập hồi quy, tỷ lệ sai số huấn luyện liên tục giảm khi độ linh hoạt tăng lên. Tuy nhiên, sai số kiểm tra thể hiện hình dáng chữ U đặc trưng, giảm lúc đầu (với mức tối thiểu tại khoảng $K = 10$) trước khi tăng trở lại khi phương pháp trở nên quá linh hoạt và bị quá khớp.

![](images/chapter_2.pdf-0028-01.png)

**HÌNH 2.17.** _Tỷ lệ sai số huấn luyện KNN (màu xanh lam, 200 quan sát) và tỷ lệ sai số kiểm tra (màu cam, 5,000 quan sát) trên dữ liệu từ Hình 2.13, khi mức độ linh hoạt (được đánh giá bằng $1/K$ trên thang log) tăng lên, hoặc tương đương khi số láng giềng $K$ giảm. Đường đứt nét màu đen biểu thị tỷ lệ sai số Bayes. Sự nhảy vọt của các đường cong là do kích thước nhỏ của tập dữ liệu huấn luyện._

Trong cả hai thiết lập hồi quy và phân loại, việc lựa chọn mức độ linh hoạt chính xác là rất quan trọng đối với sự thành công của bất kỳ phương pháp học thống kê nào. Sự đánh đổi giữa độ chệch và phương sai, và hình dáng chữ U kết quả trong sai số kiểm tra, có thể làm cho đây trở thành một nhiệm vụ khó khăn. Trong Chương 5, chúng ta quay lại chủ đề này và thảo luận về các phương pháp khác nhau để ước lượng tỷ lệ sai số kiểm tra và qua đó lựa chọn mức độ linh hoạt tối ưu cho một phương pháp học thống kê cho trước.


## 2.3 Thực hành: Giới thiệu về R 

Trong bài thực hành này, chúng tôi sẽ giới thiệu một số lệnh `R` đơn giản. Cách tốt nhất để học một ngôn ngữ mới là thử nghiệm các lệnh. `R` có thể được tải xuống từ 

#### `http://cran.r-project.org/` 

Chúng tôi khuyên bạn nên chạy `R` trong một môi trường phát triển tích hợp (IDE) như `RStudio`, phần mềm có thể được tải xuống miễn phí từ 

```
http://rstudio.com
```

2.3 Thực hành: Giới thiệu về R 43 

Trang web `RStudio` cũng cung cấp một phiên bản `R` dựa trên đám mây, không yêu cầu cài đặt bất kỳ phần mềm nào. 

### _2.3.1 Các lệnh cơ bản_ 

`R` sử dụng các _hàm_ (functions) để thực hiện các phép toán. Để chạy một hàm có tên là `funcname`, chúng ta nhập `funcname(input1, input2)`, trong đó các đầu vào (hoặc _đối số_ - arguments) `input1` và `input2` cho `R` biết cách chạy hàm. Một hàm có thể có bất kỳ số lượng đầu vào nào. Ví dụ, để tạo một vector các số, chúng ta sử dụng hàm `c()` (viết tắt của _concatenate_ - nối). Bất kỳ số nào bên trong dấu ngoặc đơn đều được nối lại với nhau. Lệnh sau đây hướng dẫn `R` nối các số 1, 3, 2 và 5 lại với nhau, và lưu chúng dưới dạng một _vector_ có tên là `x`. Khi chúng ta nhập `x`, nó sẽ trả về cho chúng ta vector đó. 

```
>x<-c(1,3,2,5)
>x
[1]1325
```

Lưu ý rằng dấu `>` không phải là một phần của lệnh; đúng hơn, nó được in ra bởi `R` để chỉ ra rằng nó đã sẵn sàng cho một lệnh khác được nhập vào. Chúng ta cũng có thể lưu các đối tượng bằng cách sử dụng `=` thay vì `<-`: 

```
>x=c(1,6,2)
>x
[1]162
>y=c(1,4,3)
```

Nhấn phím mũi tên _lên_ nhiều lần sẽ hiển thị các lệnh trước đó, các lệnh này sau đó có thể được chỉnh sửa. Điều này rất hữu ích vì người ta thường muốn lặp lại một lệnh tương tự. Ngoài ra, việc nhập `?funcname` sẽ luôn khiến `R` mở một cửa sổ tệp trợ giúp mới với thông tin bổ sung về hàm `funcname()`. 

Chúng ta có thể yêu cầu `R` cộng hai tập hợp số lại với nhau. Nó sẽ cộng số đầu tiên từ `x` với số đầu tiên từ `y`, và tiếp tục như vậy. Tuy nhiên, `x` và `y` phải có cùng độ dài. Chúng ta có thể kiểm tra độ dài của chúng bằng cách sử dụng hàm `length()`. 

```
>length(x)
[1]3
>length(y)
[1]3
>x+y
[1]2105
```

Hàm `ls()` cho phép chúng ta xem danh sách tất cả các đối tượng, chẳng hạn như dữ liệu và hàm, mà chúng ta đã lưu cho đến nay. Hàm `rm()` có thể được sử dụng để xóa bất kỳ đối tượng nào mà chúng ta không muốn. 

```
>ls()
[1]"x""y"
>rm(x,y)
```

2. Học thống kê 

44 

```
>ls()
character(0)
```

Cũng có thể xóa tất cả các đối tượng cùng một lúc: 

```
>rm(list=ls())
```

Hàm `matrix()` có thể được sử dụng để tạo một ma trận các số. Trước khi sử dụng hàm `matrix()`, chúng ta có thể tìm hiểu thêm về nó: 

```
>?matrix
```

Tệp trợ giúp cho thấy hàm `matrix()` nhận một số lượng đầu vào, nhưng hiện tại chúng ta tập trung vào ba đầu vào đầu tiên: dữ liệu (các phần tử trong ma trận), số hàng và số cột. Trước tiên, chúng ta tạo một ma trận đơn giản. 

```
>x<-matrix(data=c(1,2,3,4),nrow=2,ncol=2)
>x
[,1][,2]
[1,]13
[2,]24
```

Lưu ý rằng chúng ta cũng có thể bỏ qua việc nhập `data=`, `nrow=`, và `ncol=` trong lệnh `matrix()` ở trên: nghĩa là, chúng ta có thể chỉ cần nhập 

```
>x<-matrix(c(1,2,3,4),2,2)
```

và điều này sẽ có tác dụng tương tự. Tuy nhiên, đôi khi việc chỉ định tên của các đối số được truyền vào có thể hữu ích, vì nếu không `R` sẽ giả định rằng các đối số của hàm được truyền vào hàm theo cùng thứ tự được đưa ra trong tệp trợ giúp của hàm. Như ví dụ này minh họa, theo mặc định `R` tạo ra các ma trận bằng cách điền liên tiếp vào các cột. Ngoài ra, tùy chọn `byrow = TRUE` có thể được sử dụng để điền vào ma trận theo thứ tự các hàng. 

```
>matrix(c(1,2,3,4),2,2,byrow=TRUE)
[,1][,2]
[1,]12
[2,]34
```

Lưu ý rằng trong lệnh trên, chúng ta đã không gán ma trận cho một giá trị chẳng hạn như `x`. Trong trường hợp này, ma trận được in ra màn hình nhưng không được lưu cho các tính toán trong tương lai. Hàm `sqrt()` trả về căn bậc hai của mỗi phần tử trong một vector hoặc ma trận. Lệnh `x^2` nâng mỗi phần tử của `x` lên lũy thừa `2`; có thể sử dụng bất kỳ lũy thừa nào, bao gồm cả lũy thừa phân số hoặc số âm. 

```
>sqrt(x)
[,1][,2]
[1,]1.001.73
[2,]1.412.00
>x^2
[,1][,2]
[1,]19
[2,]416
```

2.3 Thực hành: Giới thiệu về R 45 

Hàm `rnorm()` tạo ra một vector các biến ngẫu nhiên phân phối chuẩn, với đối số đầu tiên `n` là kích thước mẫu. Mỗi lần chúng ta gọi hàm này, chúng ta sẽ nhận được một kết quả khác nhau. Ở đây, chúng ta tạo ra hai tập hợp số có tương quan với nhau, `x` và `y`, và sử dụng hàm `cor()` để tính toán hệ số tương quan giữa chúng. 

```
>x<-rnorm(50)
>y<-x+rnorm(50,mean=50,sd=.1)
>cor(x,y)
[1]0.995
```

Theo mặc định, `rnorm()` tạo ra các biến ngẫu nhiên chuẩn hóa với giá trị trung bình là 0 và độ lệch chuẩn là 1. Tuy nhiên, giá trị trung bình và độ lệch chuẩn có thể được thay đổi bằng cách sử dụng các đối số `mean` và `sd`, như được minh họa ở trên. Đôi khi chúng ta muốn mã của mình tái tạo chính xác cùng một tập hợp các số ngẫu nhiên; chúng ta có thể sử dụng hàm `set.seed()` để thực hiện điều này. Hàm `set.seed()` nhận một đối số số nguyên (tùy ý). 

```
>set.seed(1303)
>rnorm(50)
[1]-1.14401.34212.18540.53640.06320.5022-0.0004
...
```

Chúng tôi sử dụng `set.seed()` trong suốt các bài thực hành bất cứ khi nào chúng tôi thực hiện các tính toán liên quan đến các đại lượng ngẫu nhiên. Nhìn chung, điều này sẽ cho phép người dùng tái tạo các kết quả của chúng tôi. Tuy nhiên, khi các phiên bản mới của `R` ra mắt, những khác biệt nhỏ có thể phát sinh giữa cuốn sách này và đầu ra từ `R`. 

Các hàm `mean()` và `var()` có thể được sử dụng để tính giá trị trung bình và phương sai của một vector các số. Việc áp dụng `sqrt()` cho đầu ra của `var()` sẽ cho độ lệch chuẩn. Hoặc chúng ta có thể đơn giản là sử dụng hàm `sd()`. 

```
var()
sd()
```

```
>set.seed(3)
>y<-rnorm(100)
>mean(y)
[1]0.0110
>var(y)
[1]0.7329
>sqrt(var(y))
[1]0.8561
>sd(y)
[1]0.8561
```

### _2.3.2 Đồ họa_ 

Hàm `plot()` là cách chính để vẽ đồ thị dữ liệu trong `R`. Ví dụ, `plot(x, y)` tạo ra một biểu đồ phân tán (scatterplot) của các số trong `x` so với các số trong `y`. Có nhiều tùy chọn bổ sung có thể được truyền vào hàm `plot()`. Ví dụ, việc truyền vào đối số `xlab` sẽ tạo ra một nhãn trên trục _x_. Để tìm hiểu thêm thông tin về hàm `plot()`, hãy nhập `?plot`. 

46 2. Học thống kê 

```
>x<-rnorm(100)
>y<-rnorm(100)
>plot(x,y)
>plot(x,y,xlab="thisisthex-axis",
ylab="thisisthey-axis",
main="PlotofXvsY")
```

Chúng ta sẽ thường muốn lưu đầu ra của một biểu đồ `R`. Lệnh mà chúng ta sử dụng để thực hiện việc này sẽ phụ thuộc vào loại tệp mà chúng ta muốn tạo. Ví dụ, để tạo một tệp pdf, chúng ta sử dụng hàm `pdf()`, và để tạo một tệp jpeg, chúng ta sử dụng hàm `jpeg()`. 

```
jpeg()
```

```
>pdf("Figure.pdf")
>plot(x,y,col="green")
>dev.off()
nulldevice
1
```

Hàm `dev.off()` chỉ ra cho `R` rằng chúng ta đã hoàn tất việc tạo biểu đồ. Ngoài ra, chúng ta có thể đơn giản là sao chép cửa sổ biểu đồ và dán nó vào một loại tệp thích hợp, chẳng hạn như tài liệu Word. 

Hàm `seq()` có thể được sử dụng để tạo một chuỗi các số. Ví dụ, `seq(a, b)` tạo ra một vector các số nguyên nằm giữa `a` và `b`. Có nhiều tùy chọn khác: ví dụ, `seq(0, 1, length = 10)` tạo ra một chuỗi gồm `10` số cách đều nhau giữa `0` và `1`. Việc nhập `3:11` là một cách viết tắt cho `seq(3, 11)` đối với các đối số nguyên. 

```
>x<-seq(1,10)
>x
[1]12345678910
>x<-1:10
>x
[1]12345678910
>x<-seq(-pi,pi,length=50)
```

Bây giờ chúng ta sẽ tạo ra một số biểu đồ phức tạp hơn. Hàm `contour()` tạo ra một _biểu đồ đường đồng mức_ (contour plot) để biểu diễn dữ liệu ba chiều; nó giống như một bản đồ địa hình. Nó nhận ba đối số: 

1. Một vector các giá trị `x` (chiều thứ nhất), 

2. Một vector các giá trị `y` (chiều thứ hai), và 

3. Một ma trận mà các phần tử của nó tương ứng với giá trị `z` (chiều thứ ba) cho mỗi cặp tọa độ (`x`, `y`). 

Tương tự như với hàm `plot()`, có nhiều đầu vào khác có thể được sử dụng để tinh chỉnh đầu ra của hàm `contour()`. Để tìm hiểu thêm về những điều này, hãy xem tệp trợ giúp bằng cách nhập `?contour`. 

```
>y<-x
>f<-outer(x,y,function(x,y)cos(y)/(1+x^2))
>contour(x,y,f)
```

2.3 Thực hành: Giới thiệu về R 

47 

```
>contour(x,y,f,nlevels=45,add=T)
>fa<-(f-t(f))/2
```

```
>contour(x,y,fa,nlevels=15)
```

Hàm `image()` hoạt động theo cùng cách như `contour()`, ngoại trừ việc nó tạo ra một biểu đồ được mã hóa bằng màu sắc mà màu sắc của nó phụ thuộc vào giá trị `z`. Điều này được gọi là một _bản đồ nhiệt_ (heatmap), và đôi khi được sử dụng để vẽ nhiệt độ trong các dự báo thời tiết. Ngoài ra, `persp()` có thể được sử dụng để tạo ra một biểu đồ ba chiều. Các đối số `theta` và `phi` kiểm soát các góc độ mà biểu đồ được xem. 

```
>image(x,y,fa)
>persp(x,y,fa)
>persp(x,y,fa,theta=30)
>persp(x,y,fa,theta=30,phi=20)
>persp(x,y,fa,theta=30,phi=70)
>persp(x,y,fa,theta=30,phi=40)
```

### _2.3.3 Trích xuất dữ liệu bằng chỉ mục_ 

Chúng ta thường muốn kiểm tra một phần của một tập hợp dữ liệu. Giả sử rằng dữ liệu của chúng ta được lưu trữ trong ma trận `A`. 

```
>A<-matrix(1:16,4,4)
>A
[,1][,2][,3][,4]
[1,]15913
[2,]261014
[3,]371115
[4,]481216
```

Sau đó, việc nhập 

```
>A[2,3]
[1]10
```

sẽ chọn phần tử tương ứng với hàng thứ hai và cột thứ ba. Số đầu tiên sau ký hiệu dấu ngoặc vuông mở `[` luôn luôn chỉ hàng, và số thứ hai luôn luôn chỉ cột. Chúng ta cũng có thể chọn nhiều hàng và cột cùng một lúc, bằng cách cung cấp các vector làm các chỉ số. 

```
>A[c(1,3),c(2,4)]
[,1][,2]
[1,]513
[2,]715
>A[1:3,2:4]
[,1][,2][,3]
[1,]5913
[2,]61014
[3,]71115
>A[1:2,]
```

2. Học thống kê 

48 

```
[,1][,2][,3][,4]
[1,]15913
[2,]261014
>A[,1:2]
[,1][,2]
[1,]15
[2,]26
[3,]37
[4,]48
```

Hai ví dụ cuối cùng bao gồm hoặc là không có chỉ số cho các cột hoặc không có chỉ số cho các hàng. Những điều này chỉ ra rằng `R` nên bao gồm tất cả các cột hoặc tất cả các hàng tương ứng. `R` coi một hàng hoặc cột đơn lẻ của một ma trận như một vector. 

```
>A[1,]
[1]15913
```

Việc sử dụng dấu âm `-` trong chỉ số yêu cầu `R` giữ lại tất cả các hàng hoặc cột ngoại trừ những hàng hoặc cột được chỉ ra trong chỉ số. 

```
>A[-c(1,3),]
[,1][,2][,3][,4]
[1,]261014
[2,]481216
>A[-c(1,3),-c(1,3,4)]
[1]68
```

Hàm `dim()` xuất ra số hàng theo sau là số cột của một ma trận đã cho. 

```
>dim(A)
[1]44
```


### _2.3.4 Nạp dữ liệu_ 

Đối với hầu hết các phân tích, bước đầu tiên bao gồm việc nạp một tập dữ liệu vào `R`. Hàm `read.table()` là một trong những cách chính để thực hiện việc này. Tệp trợ giúp của `read.table()` chứa các thông tin chi tiết về cách sử dụng hàm này. Chúng ta có thể sử dụng hàm `write.table()` để xuất dữ liệu. 

```
write.table()
```

Trước khi thử nạp một tập dữ liệu, chúng ta phải đảm bảo rằng `R` biết tìm kiếm dữ liệu trong thư mục thích hợp. Ví dụ, trên hệ thống Windows, người ta có thể chọn thư mục bằng cách sử dụng tùy chọn `Change dir ...` trong menu `File`. Tuy nhiên, các chi tiết về cách thực hiện việc này phụ thuộc vào hệ điều hành (ví dụ: Windows, Mac, Unix) đang được sử dụng, và do đó chúng tôi không cung cấp thêm chi tiết ở đây. 

Chúng ta bắt đầu bằng cách nạp tập dữ liệu `Auto`. Dữ liệu này là một phần của thư viện `ISLR2`, được thảo luận trong Chương 3. Để minh họa cho hàm `read.table()`, bây giờ chúng ta nạp nó từ một tệp văn bản, `Auto.data`, tệp mà bạn có thể tìm thấy trên trang web của giáo trình. Lệnh sau sẽ nạp tệp `Auto.data` vào `R` và lưu trữ nó dưới dạng một đối tượng có tên là `Auto`, ở một định dạng được gọi là một _khung dữ liệu (data frame)_. data frame 

2.3 Thực hành: Giới thiệu về R 49 

Một khi dữ liệu đã được nạp, hàm `View()` có thể được sử dụng để xem nó trong một cửa sổ giống như bảng tính.<sup>1</sup> Hàm `head()` cũng có thể được sử dụng để xem một vài hàng đầu tiên của dữ liệu. 

```
>Auto<-read.table("Auto.data")
```

|`> View(Auto)`<br>`> head(Auto)`<br><br><br><br>||
|---|---|
|`V1`<br>`V2`<br>`V3`<br>`V4`|`V5`|
|`1`<br>`mpg cylinders displacement horsepower `|`weight`|
|`2 18.0`<br>`8`<br>`307.0`<br>`130.0`|`3504.`|
|`3 15.0`<br>`8`<br>`350.0`<br>`165.0`|`3693.`|
|`4 18.0`<br>`8`<br>`318.0`<br>`150.0`|`3436.`|
|`5 16.0`<br>`8`<br>`304.0`<br>`150.0`|`3433.`|
|`6 17.0`<br>`8`<br>`302.0`<br>`140.0`|`3449.`|
|`V6`<br>`V7`<br>`V8`|`V9`|
|`1 acceleration year origin`|`name`|
|`2`<br>`12.0`<br>`70`<br>`1 chevrolet chev`|`elle malibu`|
|`3`<br>`11.5`<br>`70`<br>`1`<br>`buick `|`skylark 320`|
|`4`<br>`11.0`<br>`70`<br>`1`<br>`plymout`|`h satellite`|
|`5`<br>`12.0`<br>`70`<br>`1`<br>`am`|`c rebel sst`|
|`6`<br>`10.5`<br>`70`<br>`1`|`ford torino`|



Lưu ý rằng Auto.data đơn giản là một tệp văn bản, bạn cũng có thể mở nó trên máy tính của mình bằng một trình soạn thảo văn bản tiêu chuẩn. Thường là một ý tưởng hay khi xem một tập dữ liệu bằng trình soạn thảo văn bản hoặc các phần mềm khác như Excel trước khi nạp nó vào `R`. 

Tập dữ liệu cụ thể này đã không được nạp một cách chính xác, bởi vì `R` đã giả định rằng tên của các biến là một phần của dữ liệu và do đó đã bao gồm chúng trong hàng đầu tiên. Tập dữ liệu này cũng bao gồm một số quan sát bị thiếu, được biểu thị bằng dấu chấm hỏi `?`. Các giá trị bị thiếu là một sự cố phổ biến trong các tập dữ liệu thực tế. Việc sử dụng tùy chọn `header = T` (hoặc `header = TRUE`) trong hàm `read.table()` nói cho `R` biết rằng dòng đầu tiên của tệp chứa các tên biến, và việc sử dụng tùy chọn `na.strings` nói cho `R` biết rằng bất cứ khi nào nó thấy một ký tự hoặc tập hợp các ký tự cụ thể (chẳng hạn như dấu chấm hỏi), nó nên được xử lý như một phần tử bị thiếu của ma trận dữ liệu. 

```
>Auto<-read.table("Auto.data",header=T,na.strings="?",
stringsAsFactors=T)
>View(Auto)
```

Đối số `stringsAsFactors = T` nói cho `R` biết rằng bất kỳ biến nào chứa các chuỗi ký tự đều nên được diễn giải như một biến định tính (qualitative variable), và mỗi chuỗi ký tự khác biệt đại diện cho một mức độ khác biệt của biến định tính đó. Một cách dễ dàng để nạp dữ liệu từ Excel vào `R` là lưu nó dưới dạng tệp csv (các giá trị được phân tách bằng dấu phẩy), và sau đó sử dụng hàm `read.csv()`. 

```
>Auto<-read.csv("Auto.csv",na.strings="?",stringsAsFactors=
T)
```

> 1Hàm này đôi khi có thể hơi kén chọn (finicky). Nếu bạn gặp khó khăn khi sử dụng nó, thì thay vào đó hãy thử hàm `head()`. 

50 2. Học thống kê 

```
>View(Auto)
>dim(Auto)
[1]3979
>Auto[1:4,]
```

Hàm `dim()` cho chúng ta biết rằng dữ liệu có 397 quan sát, hay các hàng, và chín biến, hay các cột. Có nhiều cách khác nhau để xử lý dữ liệu bị thiếu. Trong trường hợp này, chỉ có năm hàng chứa các quan sát bị thiếu, và do đó chúng tôi chọn sử dụng hàm `na.omit()` để đơn giản là loại bỏ các hàng này. 

```
na.omit()
```

```
>Auto<-na.omit(Auto)
>dim(Auto)
[1]3929
```

Một khi dữ liệu được nạp chính xác, chúng ta có thể sử dụng hàm `names()` để kiểm tra tên các biến. 

```
>names(Auto)
[1]"mpg""cylinders""displacement""horsepower"
[5]"weight""acceleration""year""origin"
[9]"name"
```

### _2.3.5 Các tóm tắt đồ họa và số học bổ sung_ 

Chúng ta có thể sử dụng hàm `plot()` để tạo ra các _biểu đồ phân tán (scatterplots)_ của các biến định lượng. Tuy nhiên, việc chỉ đơn giản gõ tên các biến sẽ tạo ra một thông báo lỗi, bởi vì `R` không biết phải tìm kiếm trong tập dữ liệu `Auto` cho các biến đó. 

```
>plot(cylinders,mpg)
Errorinplot(cylinders,mpg):object`cylinders 'notfound
```

Để tham chiếu đến một biến, chúng ta phải gõ tên tập dữ liệu và tên biến được nối với nhau bằng ký hiệu `$`. Thay vào đó, chúng ta có thể sử dụng hàm `attach()` để yêu cầu `R` làm cho các biến trong khung dữ liệu này có sẵn bằng tên của chúng. 

```
>plot(Auto$cylinders,Auto$mpg)
>attach(Auto)
>plot(cylinders,mpg)
```

Biến `cylinders` được lưu trữ dưới dạng một vector số, vì vậy `R` đã xử lý nó như một biến định lượng. Tuy nhiên, vì chỉ có một số ít các giá trị có thể có cho `cylinders`, người ta có thể muốn xử lý nó như một biến định tính. Hàm `as.factor()` chuyển đổi các biến định lượng thành các biến định tính. 

```
>cylinders<-as.factor(cylinders)
```

Nếu biến được vẽ trên trục $x$ là biến định tính, thì _biểu đồ hộp (boxplots)_ sẽ tự động được tạo ra bởi hàm `plot()`. Như thường lệ, một số tùy chọn có thể được chỉ định để tùy chỉnh các biểu đồ. 

2.3 Thực hành: Giới thiệu về R 51 

```
>plot(cylinders,mpg)
>plot(cylinders,mpg,col="red")
>plot(cylinders,mpg,col="red",varwidth=T)
>plot(cylinders,mpg,col="red",varwidth=T,
horizontal=T)
>plot(cylinders,mpg,col="red",varwidth=T,
xlab="cylinders",ylab="MPG")
```

Hàm `hist()` có thể được sử dụng để vẽ một _biểu đồ tần suất (histogram)_. Lưu ý rằng `col = 2` có cùng tác dụng như `col = "red"`. 

`hist()` histogram 

```
>hist(mpg)
>hist(mpg,col=2)
>hist(mpg,col=2,breaks=15)
```

Hàm `pairs()` tạo ra một _ma trận biểu đồ phân tán (scatterplot matrix)_, tức là một biểu đồ phân tán cho mọi cặp biến. Chúng ta cũng có thể tạo ra các biểu đồ phân tán chỉ cho một tập con các biến. 

<mark>`> pairs(Auto) > pairs(`</mark> _<mark>∼</mark>_ <mark>`mpg + displacement + horsepower + weight + acceleration , data = Auto )`</mark> 

Kết hợp với hàm `plot()`, hàm `identify()` cung cấp một phương pháp tương tác hữu ích để nhận dạng giá trị của một biến cụ thể cho các điểm trên một biểu đồ. Chúng ta truyền vào ba đối số cho `identify()`: biến trục $x$, biến trục $y$, và biến mà chúng ta muốn thấy giá trị của nó được in ra cho từng điểm. Sau đó, việc nhấp chuột vào một hoặc nhiều điểm trong biểu đồ và nhấn phím Escape sẽ khiến `R` in ra các giá trị của biến đang được quan tâm. Các con số được in ra dưới hàm `identify()` tương ứng với các hàng của các điểm đã chọn. 

```
identify()
```

```
>plot(horsepower ,mpg)
>identify(horsepower,mpg,name)
```

Hàm `summary()` tạo ra một tóm tắt số học của từng biến trong một tập dữ liệu cụ thể. 

```
summary()
```

|`> summary(Auto)`<br>|||
|---|---|---|
|`mpg`|`cylinders`|`displacement`|
|`Min.`<br>`: 9.00`|`Min.`<br>`:3.000`|`Min.`<br>`: 68.0`|
|`1st Qu.:17.00`|`1st Qu.:4.000`|`1st Qu.:105.0`|
|`Median :22.75`|`Median :4.000`|`Median :151.0`|
|`Mean`<br>`:23.45`|`Mean`<br>`:5.472`|`Mean`<br>`:194.4`|
|`3rd Qu.:29.00`|`3rd Qu.:8.000`|`3rd Qu.:275.8`|
|`Max.`<br>`:46.60`|`Max.`<br>`:8.000`|`Max.`<br>`:455.0`|
|`horsepower`|`weight`|`acceleration`|
|`Min.`<br>`: 46.0`|`Min.`<br>`:1613`|`Min.`<br>`: 8.00`|
|`1st Qu.: 75.0`|`1st Qu.:2225`|`1st Qu.:13.78`|
|`Median : 93.5`|`Median :2804`|`Median :15.50`|
|`Mean`<br>`:104.5`|`Mean`<br>`:2978`|`Mean`<br>`:15.54`|



52 2. Học thống kê 

|`3rd `|`Qu.:126.0`|`3rd `|`Qu.`|`:3615`|`3rd Qu.:17.02`||
|---|---|---|---|---|---|---|
|`Max.`|`:230.0`|`Max.`||`:5140`|`Max.`<br>`:24.80`||
||`year`||`ori`|`gin`||`name`|
|`Min.`|`:70.00`|`Min.`||`:1.000`|`amc matador`|`:`<br>`5`|
|`1st `|`Qu.:73.00`|`1st `|`Qu.`|`:1.000`|`ford pinto`|`:`<br>`5`|
|`Medi`|`an :76.00`|`Medi`|`an `|`:1.000`|`toyota corolla`|`:`<br>`5`|
|`Mean`|`:75.98`|`Mean`||`:1.577`|`amc gremlin`|`:`<br>`4`|
|`3rd `|`Qu.:79.00`|`3rd `|`Qu.`|`:2.000`|`amc hornet`|`:`<br>`4`|
|`Max.`|`:82.00`|`Max.`||`:3.000`|`chevrolet cheve`|`tte:`<br>`4`|
||||||`(Other)`|`:365`|



Đối với các biến định tính như `name`, `R` sẽ liệt kê số lượng các quan sát rơi vào mỗi phân loại. Chúng ta cũng có thể tạo ra một tóm tắt chỉ cho một biến duy nhất. 

```
>summary(mpg)
```

|`Min. 1st Qu.`|`Median`|`Mean `|`3rd Qu.`<br>`Max.`|
|---|---|---|---|
|`9.00`<br>`17.00`|`22.75`|`23.45`|`29.00`<br>`46.60`|



Một khi chúng ta hoàn thành việc sử dụng `R`, chúng ta gõ `q()` để tắt nó đi, hoặc thoát. Khi thoát `R`, chúng ta có tùy chọn để lưu _không gian làm việc (workspace)_ hiện tại sao cho tất cả các đối tượng (chẳng hạn như các tập dữ liệu) mà chúng ta đã tạo trong phiên làm việc `R` này sẽ có sẵn trong lần tới. Trước khi thoát `R`, chúng ta có thể muốn lưu lại một bản ghi của tất cả các lệnh mà chúng ta đã gõ trong phiên gần đây nhất; điều này có thể được hoàn thành bằng cách sử dụng hàm `savehistory()`. Lần tới khi chúng ta vào `R`, chúng ta có thể nạp lịch sử đó bằng hàm `loadhistory()`, nếu chúng ta muốn. 

```
loadhistory()
```

## 2.4 Bài tập 

### _Lý thuyết (Conceptual)_ 

1. Đối với mỗi phần từ (a) đến (d), hãy chỉ ra xem nhìn chung chúng ta kỳ vọng hiệu suất của một phương pháp học thống kê linh hoạt sẽ tốt hơn hay kém hơn so với một phương pháp không linh hoạt. Giải thích câu trả lời của bạn. 

   - (a) Kích thước mẫu $n$ cực kỳ lớn, và số lượng biến dự báo $p$ là nhỏ. 

   - (b) Số lượng biến dự báo $p$ cực kỳ lớn, và số lượng quan sát $n$ là nhỏ. 

   - (c) Mối quan hệ giữa các biến dự báo và biến phản hồi là phi tuyến tính cao. 

   - (d) Phương sai của các sai số, tức là $\sigma^2 = \text{Var}(\epsilon)$, là cực kỳ cao. 

2. Hãy giải thích xem mỗi kịch bản sau là một bài toán phân loại hay hồi quy, và chỉ ra xem chúng ta quan tâm nhất đến suy luận hay dự đoán. Cuối cùng, hãy cung cấp $n$ và $p$. 

2.4 Bài tập 53 

   - (a) Chúng ta thu thập một tập dữ liệu về 500 công ty hàng đầu ở Mỹ. Đối với mỗi công ty, chúng ta ghi nhận lợi nhuận, số lượng nhân viên, ngành công nghiệp và mức lương của CEO. Chúng ta quan tâm đến việc hiểu những yếu tố nào ảnh hưởng đến mức lương của CEO. 

   - (b) Chúng ta đang xem xét việc ra mắt một sản phẩm mới và muốn biết liệu nó sẽ _thành công_ hay _thất bại_. Chúng ta thu thập dữ liệu về 20 sản phẩm tương tự đã được ra mắt trước đó. Đối với mỗi sản phẩm, chúng ta đã ghi nhận liệu nó thành công hay thất bại, mức giá được tính cho sản phẩm, ngân sách tiếp thị, giá của đối thủ cạnh tranh, và mười biến khác. 

   - (c) Chúng ta quan tâm đến việc dự đoán sự thay đổi % trong tỷ giá hối đoái USD/Euro liên quan đến những thay đổi hàng tuần trên các thị trường chứng khoán thế giới. Do đó, chúng ta thu thập dữ liệu hàng tuần cho cả năm 2012. Đối với mỗi tuần, chúng ta ghi nhận sự thay đổi % của USD/Euro, sự thay đổi % của thị trường Mỹ, sự thay đổi % của thị trường Anh, và sự thay đổi % của thị trường Đức. 

3. Bây giờ chúng ta xem lại sự phân rã độ chệch-phương sai (bias-variance decomposition). 

   - (a) Hãy cung cấp một phác thảo về các đường cong điển hình của độ chệch (bình phương), phương sai, lỗi huấn luyện, lỗi kiểm tra, và lỗi Bayes (hoặc lỗi không thể giảm thiểu), trên cùng một đồ thị, khi chúng ta đi từ các phương pháp học thống kê ít linh hoạt hơn hướng tới các phương pháp linh hoạt hơn. Trục $x$ nên đại diện cho mức độ linh hoạt trong phương pháp, và trục $y$ nên đại diện cho các giá trị của từng đường cong. Cần có năm đường cong. Đảm bảo dán nhãn cho từng đường cong. 

- (b) Giải thích tại sao mỗi đường cong trong số năm đường cong lại có hình dạng được hiển thị ở phần (a). 

- 4. Bây giờ bạn sẽ nghĩ đến một số ứng dụng thực tế cho học thống kê. 

   - (a) Mô tả ba ứng dụng thực tế mà trong đó việc _phân loại_ có thể hữu ích. Mô tả biến phản hồi, cũng như các biến dự báo. Mục tiêu của mỗi ứng dụng là suy luận hay dự đoán? Giải thích câu trả lời của bạn. 

   - (b) Mô tả ba ứng dụng thực tế mà trong đó _hồi quy_ có thể hữu ích. Mô tả biến phản hồi, cũng như các biến dự báo. Mục tiêu của mỗi ứng dụng là suy luận hay dự đoán? Giải thích câu trả lời của bạn. 

   - (c) Mô tả ba ứng dụng thực tế mà trong đó _phân tích cụm_ có thể hữu ích. 

5. Những lợi thế và bất lợi của một phương pháp tiếp cận rất linh hoạt (so với một phương pháp ít linh hoạt hơn) đối với hồi quy hoặc phân loại là gì? Trong... 

- 54 2. Học thống kê 

...những hoàn cảnh nào thì một phương pháp linh hoạt hơn có thể được ưu tiên hơn so với một phương pháp ít linh hoạt hơn? Khi nào thì một phương pháp ít linh hoạt hơn có thể được ưu tiên? 

6. Mô tả những sự khác biệt giữa một phương pháp tiếp cận học thống kê tham số và phi tham số. Những lợi thế của một phương pháp tiếp cận tham số đối với hồi quy hoặc phân loại (trái ngược với một phương pháp phi tham số) là gì? Những bất lợi của nó là gì? 

7. Bảng dưới đây cung cấp một tập dữ liệu huấn luyện chứa sáu quan sát, ba biến dự báo, và một biến phản hồi định tính. 

|Obs.|$X_1$|$X_2$|$X_3$|$Y$|
|---|---|---|---|---|
|1|0|3|0|Red|
|2|2|0|0|Red|
|3|0|1|3|Red|
|4|0|1|2|Green|
|5|$-1$|0|1|Green|
|6|1|1|1|Red|



Giả sử chúng ta muốn sử dụng tập dữ liệu này để đưa ra một dự đoán cho $Y$ khi $X_1 = X_2 = X_3 = 0$ bằng cách sử dụng $K$-láng giềng gần nhất. 

- (a) Tính khoảng cách Euclid giữa mỗi quan sát và điểm kiểm tra, $X_1 = X_2 = X_3 = 0$. 

- (b) Dự đoán của chúng ta là gì với $K = 1$? Tại sao? 

- (c) Dự đoán của chúng ta là gì với $K = 3$? Tại sao? 

- (d) Nếu ranh giới quyết định Bayes trong bài toán này là phi tuyến tính cao, thì chúng ta có kỳ vọng giá trị _tốt nhất_ cho $K$ là lớn hay nhỏ không? Tại sao? 


### _Thực hành_ 

8. Bài tập này liên quan đến tập dữ liệu `College`, có thể được tìm thấy trong file `College.csv` trên trang web của cuốn sách. Nó chứa một số biến cho 777 trường đại học và cao đẳng khác nhau ở Mỹ. Các biến là 

   - `Private` : Chỉ báo công lập/dân lập 

   - `Apps` : Số lượng đơn đăng ký nhận được 

   - `Accept` : Số lượng người nộp đơn được chấp nhận 

   - `Enroll` : Số lượng sinh viên mới nhập học 

   - `Top10perc` : Sinh viên mới thuộc top 10% của lớp trung học 

   - `Top25perc` : Sinh viên mới thuộc top 25% của lớp trung học 

2.4 Bài tập 55 

- `F.Undergrad` : Số lượng sinh viên đại học toàn thời gian 

- `P.Undergrad` : Số lượng sinh viên đại học bán thời gian 

- `Outstate` : Học phí ngoài tiểu bang 

- `Room.Board` : Chi phí ăn ở 

- `Books` : Chi phí sách ước tính 

- `Personal` : Chi tiêu cá nhân ước tính 

- `PhD` : Phần trăm giảng viên có bằng Tiến sĩ 

- `Terminal` : Phần trăm giảng viên có bằng cấp cao nhất trong lĩnh vực (terminal degree) 

- `S.F.Ratio` : Tỷ lệ sinh viên/giảng viên 

- `perc.alumni` : Phần trăm cựu sinh viên quyên góp 

- `Expend` : Chi phí giảng dạy cho mỗi sinh viên 

- `Grad.Rate` : Tỷ lệ tốt nghiệp 

Trước khi đọc dữ liệu vào `R`, bạn có thể xem nó trong Excel hoặc một trình soạn thảo văn bản. 

- (a) Sử dụng hàm `read.csv()` để đọc dữ liệu vào `R`. Gọi dữ liệu được tải là `college`. Hãy đảm bảo rằng bạn đã đặt thư mục đến đúng vị trí của dữ liệu. 

- (b) Xem dữ liệu bằng hàm `View()`. Bạn sẽ nhận thấy rằng cột đầu tiên chỉ là tên của mỗi trường đại học. Chúng ta không thực sự muốn `R` coi đây là dữ liệu. Tuy nhiên, có thể tiện lợi khi giữ lại những cái tên này cho phần sau. Hãy thử các lệnh sau: 

```
>rownames(college)<-college[,1]
>View(college)
```

Bạn sẽ thấy hiện có một cột `row.names` ghi lại tên của mỗi trường đại học. Điều này có nghĩa là `R` đã đặt tên cho mỗi hàng tương ứng với trường đại học thích hợp. `R` sẽ không cố gắng thực hiện tính toán trên tên các hàng. Tuy nhiên, chúng ta vẫn cần loại bỏ cột đầu tiên trong dữ liệu, nơi lưu trữ các tên. Hãy thử 

```
>college<-college[,-1]
>View(college)
```

Bây giờ bạn sẽ thấy rằng cột dữ liệu đầu tiên là `Private`. Lưu ý rằng một cột khác có nhãn `row.names` hiện xuất hiện trước cột `Private`. Tuy nhiên, đây không phải là một cột dữ liệu mà là tên mà `R` đang đặt cho mỗi hàng. 

- (c) i. Sử dụng hàm `summary()` để tạo một bản tóm tắt bằng số của các biến trong tập dữ liệu. 

56 2. Học thống kê 

- ii. Sử dụng hàm `pairs()` để tạo ma trận biểu đồ phân tán của mười cột hoặc biến đầu tiên của dữ liệu. Nhớ lại rằng bạn có thể tham chiếu đến mười cột đầu tiên của một ma trận `A` bằng cách sử dụng `A[,1:10]`. 

- iii. Sử dụng hàm `plot()` để tạo các biểu đồ hộp nằm cạnh nhau của `Outstate` so với `Private`. 

- iv. Tạo một biến định tính mới, được gọi là `Elite`, bằng cách _nhóm_ biến `Top10perc`. Chúng ta sẽ chia các trường đại học thành hai nhóm dựa trên việc tỷ lệ sinh viên đến từ top 10% của các lớp trung học của họ có vượt quá 50% hay không. 

```
>Elite<-rep("No",nrow(college))
>Elite[college$Top10perc>50]<-"Yes"
>Elite<-as.factor(Elite)
>college<-data.frame(college,Elite)
```

Sử dụng hàm `summary()` để xem có bao nhiêu trường đại học ưu tú. Bây giờ hãy sử dụng hàm `plot()` để tạo các biểu đồ hộp nằm cạnh nhau của `Outstate` so với `Elite`. 

      - v. Sử dụng hàm `hist()` để tạo một số biểu đồ tần suất với số lượng nhóm khác nhau cho một vài biến định lượng. Bạn có thể thấy lệnh `par(mfrow = c(2, 2))` hữu ích: nó sẽ chia cửa sổ in thành bốn khu vực để có thể vẽ đồng thời bốn biểu đồ. Sửa đổi các đối số cho hàm này sẽ chia màn hình theo những cách khác. 

      - vi. Tiếp tục khám phá dữ liệu và cung cấp một bản tóm tắt ngắn gọn về những gì bạn phát hiện ra. 

9. Bài tập này liên quan đến tập dữ liệu `Auto` đã được nghiên cứu trong phần thực hành. Hãy chắc chắn rằng các giá trị bị khuyết đã được loại bỏ khỏi dữ liệu. 

   - (a) Trong số các biến dự báo, biến nào là định lượng và biến nào là định tính? 

   - (b) _Khoảng_ của mỗi biến dự báo định lượng là bao nhiêu? Bạn có thể trả lời câu hỏi này bằng cách sử dụng hàm `range()`. 

   - `range()` 

- (c) Giá trị trung bình và độ lệch chuẩn của mỗi biến dự báo định lượng là bao nhiêu? 

- (d) Bây giờ hãy loại bỏ các quan sát từ thứ 10 đến thứ 85. Khoảng, giá trị trung bình và độ lệch chuẩn của mỗi biến dự báo trong tập con dữ liệu còn lại là bao nhiêu? 

- (e) Sử dụng tập dữ liệu đầy đủ, hãy điều tra các biến dự báo bằng đồ thị, sử dụng biểu đồ phân tán hoặc các công cụ khác mà bạn chọn. Tạo một số biểu đồ làm nổi bật các mối quan hệ giữa các biến dự báo. Nhận xét về những phát hiện của bạn. 

2.4 Bài tập 57 

   - (f) Giả sử rằng chúng ta muốn dự đoán mức tiêu thụ nhiên liệu (`mpg`) dựa trên các biến khác. Các biểu đồ của bạn có gợi ý rằng bất kỳ biến nào khác có thể hữu ích trong việc dự đoán `mpg` hay không? Biện minh cho câu trả lời của bạn. 

10. Bài tập này liên quan đến tập dữ liệu nhà ở `Boston`. 

   - (a) Để bắt đầu, hãy tải tập dữ liệu `Boston`. Tập dữ liệu `Boston` là một phần của _thư viện_ `ISLR2`. 

```
>library(ISLR2)
```

Bây giờ tập dữ liệu được chứa trong đối tượng `Boston`. 

```
>Boston
```

Đọc về tập dữ liệu: 

```
>?Boston
```

Có bao nhiêu hàng trong tập dữ liệu này? Có bao nhiêu cột? Các hàng và các cột đại diện cho điều gì? 

- (b) Tạo một số biểu đồ phân tán theo cặp của các biến dự báo (các cột) trong tập dữ liệu này. Mô tả những phát hiện của bạn. 

- (c) Có bất kỳ biến dự báo nào liên quan đến tỷ lệ tội phạm bình quân đầu người không? Nếu có, hãy giải thích mối quan hệ. 

- (d) Có bất kỳ khu vực điều tra dân số nào của Boston dường như có tỷ lệ tội phạm đặc biệt cao không? Thuế suất? Tỷ lệ học sinh-giáo viên? Nhận xét về khoảng của mỗi biến dự báo. 

- (e) Có bao nhiêu khu vực điều tra dân số trong tập dữ liệu này giáp với sông Charles? 

- (f) Tỷ lệ học sinh-giáo viên trung vị giữa các thị trấn trong tập dữ liệu này là bao nhiêu? 

- (g) Khu vực điều tra dân số nào của Boston có giá trị trung vị thấp nhất cho những ngôi nhà do chủ sở hữu cư trú? Các giá trị của các biến dự báo khác cho khu vực điều tra dân số đó là bao nhiêu, và những giá trị đó so sánh như thế nào với các khoảng tổng thể cho những biến dự báo đó? Nhận xét về những phát hiện của bạn. 

- (h) Trong tập dữ liệu này, có bao nhiêu khu vực điều tra dân số trung bình có hơn bảy phòng cho mỗi chỗ ở? Hơn tám phòng cho mỗi chỗ ở? Nhận xét về các khu vực điều tra dân số trung bình có hơn tám phòng cho mỗi chỗ ở. 


![](images/chapter_2.pdf-0044-00.png)


