/* 다크/라이트 모드 플로팅 토글 버튼.
 * head/custom.html이 미리 data-theme를 적용해 두므로 여기는 UI만 담당. */
(function () {
  var KEY = 'lmw-theme';

  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') || 'light';
  }

  function setTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem(KEY, t); } catch (e) {}
  }

  function mount() {
    if (document.querySelector('.theme-toggle')) return;

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'theme-toggle';
    btn.setAttribute('aria-label', '다크 모드 전환');

    function render() {
      var t = currentTheme();
      btn.textContent = t === 'dark' ? '☀' : '☾';
      btn.setAttribute(
        'title',
        t === 'dark' ? '라이트 모드로 전환' : '다크 모드로 전환'
      );
      btn.setAttribute('aria-pressed', t === 'dark' ? 'true' : 'false');
    }

    btn.addEventListener('click', function () {
      setTheme(currentTheme() === 'dark' ? 'light' : 'dark');
      render();
    });

    render();
    document.body.appendChild(btn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
