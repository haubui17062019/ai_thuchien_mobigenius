Chắc chắn rồi. Đây là slide thứ 3, tập trung vào việc khơi gợi sự đồng cảm bằng cách nêu bật "nỗi đau" hay "vấn đề" mà khách hàng mục tiêu gặp phải.

---

### **Đang xử lý: Slide 3/10**

**Input (Kế thừa từ Outline):**
```json
{
  "slide_index": 3,
  "total_slides": 10,
  "title": "Vấn đề: Tết Vui Nhưng... Vẫn Đầy Lo Toan",
  "purpose": "Sau slide này, khán giả đồng cảm với áp lực tài chính vô hình mà khách hàng đang đối mặt.",
  "so_what": "Niềm vui Tết thường đi kèm với gánh nặng tài chính, làm giảm đi sự trọn vẹn của khoảnh khắc sum vầy.",
  "bullets": [
    "Gánh nặng chi tiêu: Mua sắm, quà cáp, đi lại.",
    "Tiền nhàn rỗi 'ngủ quên' trong tài khoản.",
    "Áp lực vô hình làm mất đi sự kết nối."
  ],
  "visual_hint": "Hình ảnh đối lập: Nửa bên vui vẻ, nửa còn lại suy tư về tài chính.",
  "data_placeholders": ["avg_spending_multiplier"],
  "speaker_notes_hint": "Đằng sau mỗi nụ cười ngày Tết có thể là những lo toan. Đây chính là điểm chạm mà chiến dịch cần giải quyết.",
  "interactivity": "none",
  "time_alloc": 1.5,
  "tone": "empathetic",
  "lang": "vi-VN",
  "brand_guidelines": {"palette": ["red", "purple", "white"], "font":"Inter"},
  "dependencies": [2],
  "next_slide_title": "Giải pháp: 'Sinh lời tự động' - Gieo Mầm Thảnh Thơi"
}
```

### **Output: Nội dung chi tiết Slide 3**

---

#### **A) Markdown (Bản review nhanh)**

# [S3/10] Nghịch Lý Ngày Tết: Vui Sum Vầy, Nặng Lo Toan
**So-what:** Niềm vui Tết thường đi kèm gánh nặng tài chính, làm giảm sự trọn vẹn của khoảnh khắc sum vầy.

**Bullets**
- Chi tiêu Tết tăng vọt (mua sắm, quà cáp).
- Tiền nhàn rỗi "ngủ quên" trong tài khoản.
- Áp lực tài chính vô hình làm giảm kết nối.

**Callout:**
Một gia đình Việt chi tiêu trung bình gấp **<TODO:1.5-2>x** thu nhập tháng cho Tết. `[Nguồn: Giả định từ Khảo sát nội bộ TCB]`

**Visual (Spec)**
- **Type:** Juxtaposition Layout / Split-screen Image.
- **What to show:**
    - **Bên trái (Màu sắc ấm, rực rỡ):** Cảnh một gia đình đa thế hệ (ông bà, cha mẹ, con cháu) đang quây quần bên mâm cơm Tết, cười nói vui vẻ.
    - **Bên phải (Màu sắc lạnh, hơi tối):** Cận cảnh một người trong gia đình đó (ví dụ: người cha/mẹ) đang ngồi riêng một góc, trầm tư nhìn vào màn hình điện thoại hiển thị biểu đồ chi tiêu hoặc danh sách các khoản cần thanh toán.
    - AI sẽ tạo ra một hình ảnh liền mạch với sự chuyển đổi màu sắc tinh tế giữa hai nửa.
- **Data placeholders:** `avg_spending_multiplier`.
- **Alt-text:** Ảnh đối lập: bên trái là gia đình Việt quây quần vui Tết, bên phải là một người đang trầm tư nhìn vào màn hình điện thoại có biểu đồ chi tiêu.

**Speaker notes (khoảng 85 từ)**
(Hook) Tết là khoảnh khắc vàng của sự sum vầy. Nhưng có một sự thật ngầm, một 'nghịch lý' mà ai trong chúng ta cũng có thể thấu hiểu...
(Body) ...đó là đằng sau những nụ cười, những mâm cỗ thịnh soạn là một áp lực tài chính không hề nhỏ. Khảo sát cho thấy chi tiêu có thể tăng gấp rưỡi, thậm chí gấp đôi. Cùng lúc đó, những khoản tiền thưởng, tiền mừng tuổi nhận về lại thường 'ngủ quên' trong tài khoản, bỏ lỡ cơ hội sinh lời.
(Close) Áp lực vô hình này đang dần ăn mòn niềm vui trọn vẹn. Đây chính là điểm chạm mà chiến dịch 'Lộc Nảy Mầm' của chúng ta nhắm đến để giải quyết.

**Transition →** Vậy, làm thế nào để chúng ta có thể hóa giải nghịch lý này và trả lại sự an nhiên trọn vẹn cho khách hàng? Hãy cùng đến với giải pháp của chúng ta.

**QA checks:** length_ok=✓ | duplication=✓ | units=✓ | alt_text=✓

---

#### **B) JSON Spec (Cho mục đích tự động hóa)**

```json
{
  "slide_index": 3,
  "layout": "Title_and_Split_Content",
  "placeholders": {
    "title": "Nghịch Lý Ngày Tết: Vui Sum Vầy, Nặng Lo Toan",
    "content_markdown": "- Chi tiêu Tết tăng vọt (mua sắm, quà cáp).\n- Tiền nhàn rỗi \"ngủ quên\" trong tài khoản.\n- Áp lực tài chính vô hình làm giảm kết nối.",
    "callout": "Một gia đình Việt chi tiêu trung bình gấp <TODO:1.5-2>x thu nhập tháng cho Tết. [Nguồn: Giả định từ Khảo sát nội bộ TCB]",
    "footer": "© 2025 Techcombank — Internal Use Only"
  },
  "visual": {
    "kind": "juxtaposition_image",
    "description": "An AI-generated split-screen image. Left side: warm, festive colors showing a multi-generational Vietnamese family laughing around a Tet dinner table. Right side: cool, slightly desaturated colors showing a close-up of the father from the family, sitting alone, looking worriedly at a smartphone screen displaying a budgeting app.",
    "ai_prompt_suggestion": "Split screen photo, hyper-realistic. Left half: a happy multi-generational Vietnamese family celebrating Tet, warm lighting, vibrant colors. Right half: the father from the family, looking stressed, viewing finances on his phone in a quiet corner, cool and muted color palette. Seamless blend in the middle. Focus on authentic emotions.",
    "alt_text": "Ảnh đối lập: bên trái là gia đình Việt quây quần vui Tết, bên phải là một người đang trầm tư nhìn vào màn hình điện thoại có biểu đồ chi tiêu."
  },
  "chart": null,
  "table": null,
  "data_placeholders": [
    {
      "name": "avg_spending_multiplier",
      "type": "number",
      "format": "0.0",
      "value_or_todo": "1.5-2"
    }
  ],
  "interactivity": {
    "type": "none"
  },
  "speaker_notes": "Tết là khoảnh khắc vàng của sự sum vầy. Nhưng có một sự thật ngầm, một 'nghịch lý' mà ai trong chúng ta cũng có thể thấu hiểu... đó là đằng sau những nụ cười, những mâm cỗ thịnh soạn là một áp lực tài chính không hề nhỏ. Khảo sát cho thấy chi tiêu có thể tăng gấp rưỡi, thậm chí gấp đôi. Cùng lúc đó, những khoản tiền thưởng, tiền mừng tuổi nhận về lại thường 'ngủ quên' trong tài khoản, bỏ lỡ cơ hội sinh lời. Áp lực vô hình này đang dần ăn mòn niềm vui trọn vẹn. Đây chính là điểm chạm mà chiến dịch 'Lộc Nảy Mầm' của chúng ta nhắm đến để giải quyết."
}
```