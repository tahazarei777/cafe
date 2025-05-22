document.addEventListener('DOMContentLoaded', function() {
  // ------------ انتخاب المان‌ها با بررسی وجود آن‌ها ------------
  const btnShowPara = document.querySelector(".btn-show-para");
  const paraElemShow = document.getElementById("paraElemShow");
  const bannerImgElem = document.querySelectorAll(".banner-img");
  const leftProductArrow = document.querySelector(".fa-caret-left");
  const rightProductArrow = document.querySelector(".fa-caret-right");
  const productCardsElem = document.querySelector(".product-cards");
  const cardElem = document.querySelector(".product-card");
  
  const bannerElem = document.querySelector(".banner");
  const bannerIMG1 = document.getElementById("banner-img-1");
  const bannerIMG2 = document.getElementById("banner-img-2");

  // ------------ تنظیمات اولیه ------------
  let indexImg = 0;
  const bannerImg = bannerImages; // فرض می‌کنیم متغیر bannerImages در HTML تعریف شده

  // ------------ بررسی وجود المان‌ها قبل از استفاده ------------
  // تنظیم عکس‌های بنر
  if (bannerIMG1 && bannerIMG2 && STATIC_PATHS) {
      bannerIMG1.src = STATIC_PATHS.banner1;
      bannerIMG2.src = STATIC_PATHS.banner2;
  }

  // ------------ عملکرد دکمه نمایش پاراگراف ------------
  if (btnShowPara && paraElemShow) {
      btnShowPara.addEventListener("click", function(e) {
          this.classList.toggle("show-para-btn");
          paraElemShow.classList.toggle("show-para-p");
      });
  }

  // ------------ اسلایدر بنر (بهینه‌شده) ------------
  if (bannerImgElem.length > 0 && bannerElem) {
      const slider = setInterval(function() {
          if (window.innerWidth >= 768) {
              clearInterval(slider);
              // نمایش همزمان دو بنر در دسکتاپ
              bannerImgElem[0].src = bannerImg[0];
              bannerImgElem[1].src = bannerImg[1];
          } else {
              // انیمیشن اسلاید برای موبایل
              indexImg = (indexImg + 1) % bannerImg.length;
              
              bannerElem.style.transition = "all 0.5s ease-in-out";
              bannerElem.style.transform = "translateX(300%)";

              setTimeout(() => {
                  bannerElem.style.transform = "translateX(0)";
                  // فقط تصویر فعال را تغییر دهید
                  bannerImgElem.forEach((img, i) => {
                      img.src = bannerImg[indexImg];
                      img.alt = 'banner ${indexImg + 1}';
                  });
              }, 500);
          }
      }, 4000);
  }

  // ------------ اسکرول کارت‌های محصول (بهینه‌شده) ------------
  if (leftProductArrow && rightProductArrow && productCardsElem && cardElem) {
      const cardElemWidth = cardElem.clientWidth + 15;
      
      leftProductArrow.addEventListener("click", () => {
          productCardsElem.scrollBy({
              left: -cardElemWidth,
              behavior: "smooth" // اضافه کردن اسکرول نرم
          });
      });

      rightProductArrow.addEventListener("click", () => {
          productCardsElem.scrollBy({
              left: cardElemWidth,
              behavior: "smooth" // اضافه کردن اسکرول نرم
          });
      });
  }
});