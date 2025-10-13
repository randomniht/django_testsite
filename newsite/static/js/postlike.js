document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.like-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            const articleId = this.dataset.articleId;
            fetch(`/articles/${articleId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({})
            })
            .then(res => {
                if (!res.ok) {
                    if (res.status === 403) {
                        alert('Пожалуйста, войдите в систему, чтобы поставить лайк.');
                    }
                    throw new Error(`Ошибка запроса: ${res.status}`);
                }
                return res.json()
            })
            .then(data => {
                const likeCountSpan = document.getElementById(`like-count-${articleId}`);
                if (likeCountSpan) {
                    likeCountSpan.innerText = data.likes;
                }
                if ('liked' in data && !data.liked) {
                    alert('Вы уже лайкали эту статью');
                }
            })
            .catch(e => console.error(e));
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}