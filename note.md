## 1. Bản chất toán học của hệ số tương quan $r$

* **Công thức gốc:**

$$r = \frac{\text{Cov}(X, Y)}{\text{SD}_X \times \text{SD}_Y} = E[Z_X \cdot Z_Y]$$


* **Ý nghĩa:** $r$ là hiệp biến (Covariance) đã được **chuẩn hóa** bằng cách chia cho tích hai độ lệch chuẩn ($\text{SD}$).
* **Tính chất cốt lõi:**
1. **Khống chế biên độ:** $-1 \le r \le 1$ (theo bất đẳng thức Cauchy-Schwarz).
2. **Không có đơn vị tính (Scale Invariance):** Bất biến khi đổi đơn vị đo hoặc cộng/nhân với hằng số dương ($y \to ay + b$ với $a > 0$).
3. **Ý nghĩa hình học:** $r = \cos(\theta)$, trong đó $\theta$ là góc giữa hai vectơ dữ liệu đã trừ giá trị trung bình.



---

## 2. $r$ và hình dáng trực quan trên biểu đồ phân tán (Scatter Plot)

* **Độ tập trung tương đối:** $r$ đo độ gom tụ của các điểm xung quanh **Đường SD** theo đơn vị tương đối (so với SD), không đo khoảng cách tuyệt đối (cm, kg...).
* **Độ xòe thực tế (r.m.s vertical distance):**

$$\text{Khoảng cách dọc r.m.s tới đường SD} = \sqrt{2(1 - \vert{}r\vert{})} \times \text{SD}_Y$$


* Ngay cả khi $r = 0.95$, độ chệch dọc của các điểm vẫn chiếm khoảng **$30\%$ của $\text{SD}_Y$**. Vì vậy, thị giác vẫn thấy dữ liệu có độ xòe/nở rõ rệt chứ không nằm trên một đường mỏng dính.



---

## 3. Các trường hợp KHÔNG NÊN dùng hoặc dễ hiểu lầm về $r$

$r$ chỉ phản ánh đúng bản chất khi dữ liệu có dạng **đám mây hình elip đồng nhất (football-shaped)**. Cần tránh các "bẫy" sau:

### a. Mối quan hệ phi tuyến (Non-linear)

$r$ chỉ đo độ tương quan **tuyến tính (đường thẳng)**, không đo mối quan hệ đường cong:

* **Dạng vòm đối xứng (U-shape/Parabol 2 nhánh):** $r \approx 0$ dù $x$ và $y$ có mối quan hệ phụ thuộc hoàn toàn (nhánh tăng triệt tiêu nhánh giảm).
* **Parabol 1 nhánh đơn điệu (như $A = \frac{1}{4}\pi d^2$ với $d \ge 0$):** $r \approx 0.97$ ("nearly 1"). Con số này cao vì đường thẳng xấp xỉ một nhánh tăng khá tốt, nhưng $r \neq 1.0$ vì $r$ "phạt" độ cong của parabol.

### b. Điểm ngoại lệ (Outliers)

Một điểm dị biệt duy nhất nằm xa đám mây dữ liệu có thể kéo tụt $r$ từ $1.0$ xuống gần $0$ (hoặc ngược lại làm xuất hiện tương quan giả).

### c. Dữ liệu chia cụm (Clusters / Sub-populations)

Gộp hai hay nhiều nhóm dân số rời rạc (ví dụ: học sinh thường vs cầu thủ bóng rổ, nam vs nữ) sẽ làm con số $r$ tổng thể bị **bóp méo**:

* Nếu 2 cụm xếp nối tiếp theo đường chéo đi lên $\rightarrow$ $r$ tổng thể **tăng lên**.
* Nếu 2 cụm bị lệch ngược hướng $\rightarrow$ $r$ tổng thể **giảm xuống hoặc đảo dấu** (Nghịch lý Simpson).

### d. Tương quan sinh thái (Ecological Correlation) & Ngụy biện sinh thái

* **Định nghĩa:** Tính $r$ dựa trên **số liệu trung bình / tỷ lệ của tập thể** (tiểu bang, quận, quốc gia) thay vì cá nhân.
* **Bản chất:** Phép lấy giá trị trung bình **triệt tiêu hoàn toàn sự phân tán trong nội bộ nhóm** (within-group variation).
* **Hậu quả:** $r_{\text{sinh thái}}$ thường **bị thổi phồng cao hơn rất nhiều** so với $r_{\text{cá nhân}}$. Việc dùng tương quan tập thể để quy chụp cho hành vi cá nhân gọi là *Ngụy biện sinh thái (Ecological Fallacy)*.

---

## 4. Các bẫy phiên giải dữ liệu thực tế (Critical Thinking)

1. **Dữ liệu cắt ngang (Cross-sectional) vs Dữ liệu dọc (Longitudinal):**
* Tương quan âm giữa tuổi và học vấn ($r = -0.20$) phản ánh **Hiệu ứng thế hệ** (thế hệ sinh ra trước có ít cơ hội học tập hơn), không có nghĩa là *cá nhân già đi thì bị mất bớt học vấn*.


2. **Thiên vị tự chọn (Selection Bias):**
* Tương quan âm giữa điểm SAT trung bình và tỷ lệ học sinh dự thi của các bang ($r = -0.84$) là do các bang tỷ lệ thi thấp chỉ gồm nhóm học sinh tinh hoa tự chọn đăng ký dự thi.


3. **Dữ liệu rời rạc (Discrete grid):**
* Số năm đi học dạng số nguyên tạo thành các sọc ngang/dọc; các điểm có cùng tọa độ sẽ bị đè lên nhau (overlapping dots) khiến số chấm nhìn thấy ít hơn số quan sát thực tế.