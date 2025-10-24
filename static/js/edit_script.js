const toast = document.getElementById("toast");
const msg = document.getElementById("toast-message");
const icon = toast.querySelector("i");
const inputElements = document.querySelectorAll(".input-floating");

// message right-bottom on site
function showToast(message, isError = false) {
  msg.textContent = message;
  icon.className = isError ? "fas fa-times" : "fas fa-check";
  toast.classList.toggle("error", isError);
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 3000);
}

// upload file for profile photo
document
  .getElementById("id_profile_image")
  ?.addEventListener("change", function (event) {
    const input = event.target;
    if (input.files && input.files[0]) {
      const reader = new FileReader();
      reader.onload = function (e) {
        document.getElementById("profile-image-preview").src = e.target.result;
        showToast("عکس جدید انتخاب شد");
      };
      reader.readAsDataURL(input.files[0]);
    }
  });


// floating label
inputElements.forEach((input) => {
  input.addEventListener("focus", (e) => {
    let parentTarget = e.target.parentElement;

    parentTarget.classList.add("floating-label");
  });

  input.addEventListener("blur", (e) => {
    let targetValue = e.target.value;
    let parentTarget = e.target.parentElement;

    if (!targetValue) {
      parentTarget.classList.remove("floating-label");
    }
  });
});

//! what is it?
// {% if messages %}
//     {% for message in messages %}
//         showToast("{{ message }}", "{{ message.tags }}" == "error");
//     {% endfor %}
// {% endif %}
