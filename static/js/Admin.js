document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', function () {
          const orderId = this.dataset.orderId;
          const card = this.closest('.card-order');
        
          if (confirm('آیا مطمئنی که می‌خوای این سفارش رو حذف کنی؟')) {
            fetch('/admin/orders/delete/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              },
              body: `order_id=${orderId}`,
            })
            .then(res => res.json())
            .then(data => {
              if (data.success) {
                card.remove();  // حذف کارت از DOM
              } else {
                alert('خطا: ' + data.error);
              }
            })
            .catch(err => {
              alert('مشکلی در حذف سفارش پیش آمد');
              console.error(err);
            });
          }
        });
      });