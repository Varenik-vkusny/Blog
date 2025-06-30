document.addEventListener('DOMContentLoaded', function() {

    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {

        button.addEventListener('click', async function() {
            const postId = this.dataset.postId;
            const likeIcon = this.querySelector('.like-icon');
            const likeCountSpan = this.querySelector('.like-count');

            try {
                const response = await fetch(`/api/post/${postId}/like`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken
                }

                })

                if (!response.ok) {
                    window.location.href = '/auth/login';
                    return;
                }

                const data = await response.json();

                likeCountSpan.textContent = data.likes;

                if (data.liked) {
                    likeIcon.textContent = '❤️';
                } else {
                    likeIcon.textContent = '🤍';
                }
            } catch (error) {
                console.error('Сетевая ошибка:', error);
            }
        });
    });
});