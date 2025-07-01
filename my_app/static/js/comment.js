document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('comment-form');
    if (!commentForm) return;
    const commentContainer = document.getElementById('comments-container');
    const commentError = document.getElementById('comment-error');
    const commentCountSpan = document.getElementById('comment-count');

    commentForm.addEventListener('submit', async function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        const commentText = formData.get('text');
        const csrfToken = formData.get('csrf_token');
        const postId = this.dataset.postId;

        if (!commentText) {
            showError('Комментарий не может быть пустым');
            return;
        }

        try {
            const response = await fetch(`/api/post/${postId}/comment`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: commentText })
            });

            const data = await response.json();

            if (response.status === 201) {
                const newComment = createCommentElement(data);
                commentContainer.insertAdjacentHTML('beforeend', newComment);
                this.reset();
                commentCountSpan.textContent = parseInt(commentCountSpan.textContent) + 1;
                hideError();
            }
            else {
                const errorMessage = data[0]?.msg || data.error || 'Произошла неизвестная ошибка';
                showError(errorMessage);
            }        
        }
        catch (error) {
            console.error('Сетевая ошибка:', error);
            showError('Не удалось отправить комментарий. Пожалуйста, попробуйте позже.');
        }
    })

    function createCommentElement(commentData) {
        return `
            <div class="comment" id="comment-${commentData.id}">
                <p><strong>${escapeHtml(commentData.author.username)}</strong> <small>${commentData.date_created}</small></p>
                <p>${commentData.text}</p>
            </div>        
        `
    }

    function showError(message) {
        commentError.textContent = message;
        commentError.style.display = 'block';
    }   

    function hideError() {
        commentError.textContent = '';
        commentError.style.display = 'none';
    }

    function escapeHtml(str) {
        const p = document.createElement('p');
        p.appendChild(document.createTextNode(str));
        return p.innerHTML;
    }
})