// static/js/like.js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.like-button').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Предотвращаем переход по ссылке

            const pointId = this.getAttribute('data-point-id');

            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

            fetch(`/like_point/${pointId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,  // Используйте токен из meta-тега
                    'Content-Type': 'application/json'
                },
                credentials: 'include'
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked) {
                    this.innerHTML = '❤️'; // Красное сердечко
                } else {
                    this.innerHTML = '🤍'; // Белое сердечко
                }
                // Обновляем количество лайков
                const likeCountElement = document.querySelector(`#like-count-${pointId}`);
                if (likeCountElement) {
                    likeCountElement.textContent = data.like_count;
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});