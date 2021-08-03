const copyBtn = document.querySelector('.copy_btn');

$(function() {
    let url = window.location.href;
    let img = $('.result_img img').attr('src');
    $("meta[property='og\\:url']").attr("content", url);
    $("meta[property='og\\:image']").attr("content", img);
});

function copyUrl() {
    let url = window.location.href;
    let tmp = document.createElement('input');
    
    document.body.appendChild(tmp);
    tmp.value = url;
    tmp.select();
	  document.execCommand("copy");
    document.body.removeChild(tmp);
    
	  alert("URL이 복사되었습니다");
}

copyBtn.addEventListener('click', copyUrl);