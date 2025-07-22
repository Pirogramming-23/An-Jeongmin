const requestLike = new XMLHttpRequest();

const onClickLike = (postId) => {
    const post = document.querySelector(`.post[data-post-id="${postId}"]`);
    const changedheartIcon = post.querySelector(".heart-icon");

    // 좋아요 아이콘 변경
    changedheartIcon.src = "https://img.icons8.com/sf-ultralight-filled/24/FA5252/hearts.png";

    const requestLike = new XMLHttpRequest();
    requestLike.open("POST", `/like/${postId}`);
    requestLike.setRequestHeader("Content-Type", "application/json");
    requestLike.send(JSON.stringify({ id: postId }));

    requestLike.onreadystatechange = () => {
        if (requestLike.readyState === XMLHttpRequest.DONE && requestLike.status === 200) {
        const response = JSON.parse(requestLike.responseText);
        const likeElement = post.querySelector(".update_like");
        likeElement.textContent = `좋아요 ${response.like_count}개`;
        }
    };
};

function onClickComment() {
    const inputField = document.querySelector(".comment_input");
    const inputValue = inputField.value.trim();

    const commentParent = document.querySelector(".uploaded_comment_container");

    const newComment = document.createElement("div");
    newComment.classList.add("upload_comment");

    newComment.innerHTML = `
        <div class="commet_user">piro</div>
        <div class="comment_content">${inputValue}</div>
        <span class="delete_comment_btn"
            onclick="onClickDelete(this)"
            style="color: #FA5252; cursor: pointer; font-size: 14px;">
        삭제
        </span>
    `;

    commentParent.appendChild(newComment);
    inputField.value = "";
}

function onClickDelete(this_comment) {
    const want_delete = this_comment.closest(".upload_comment");
    const alert = confirm("해당 댓글을 삭제하시겠습니까?");
    if (alert) {
        want_delete.remove();
    }
}
