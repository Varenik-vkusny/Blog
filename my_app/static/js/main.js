document.addEventListener('DOMContentLoaded', function() {

    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {

        button.addEventListener('click', async function() {
            const postId = this.dataset.postId;
            const heartIcon = this.querySelector('.heart-svg');
            const likeCountSpan = this.querySelector('.like-count');

            try {
                const response = await fetch(`/api/post/${postId}/like`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken
                    }
                });

                

                if (!response.ok) {
                    window.location.href = '/auth/login';
                    return;
                }

                const data = await response.json();

                likeCountSpan.textContent = data.likes;

                if (data.liked) {
                    heartIcon.setAttribute('fill', 'red');
                } else {
                    heartIcon.setAttribute('fill', 'none');
                }
            } catch (error) {
                console.error('Сетевая ошибка:', error);
            }
        });
    });
});