let deferredPrompt;

export function CreateBtn(id = 'downloadPWA') {
  const btnContainer = document.getElementById(id);

  const btn = document.createElement('div');
  btn.id = 'btn-install-button';
  btn.className = 'd-flex justify-content-center align-items-center reset-Padding div-btn-app';

  btn.innerHTML = `
    <svg id="download-icon" xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="d-lg-none feather-download" style="margin-left: 10px;">
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
      <polyline points="7 10 12 15 17 10"></polyline>
      <line x1="12" y1="15" x2="12" y2="3"></line>
    </svg>
    <button id="install-button" class="w-100 text-uppercase text-white fw-bolder reset-Padding" style="display:none;">Baixar APP</button>
  `;

  btnContainer.appendChild(btn);

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;

    document.getElementById('install-button').style.display = 'block';
  });

  window.addEventListener('appinstalled', (evt) => {
    console.log('PWA instalado');

    const items = document.querySelectorAll('.div-btn-app');
    items.forEach((e) => {
      console.log(e);
      e.style.display = 'none';
    });

    document.getElementById('install-button').style.display = 'none';
    document.getElementById('btn-install-button').classList.add('d-none'); // Oculta o botão quando o PWA está instalado
  });

  document.getElementById('install-button').addEventListener('click', () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('Usuário aceitou instalar o PWA');
        } else {
          console.log('Usuário recusou instalar o PWA');
        }
        deferredPrompt = null;
      });
    }
  });

  // Verifica se o PWA já está instalado
  window.addEventListener('load', () => {
    if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true) {
      document.getElementById('install-button').style.display = 'none';
      document.getElementById('btn-install-button').classList.add('d-none'); // Oculta o botão quando o PWA está instalado
    } else {
      document.getElementById('install-button').style.display = 'block';
    }
  });
}
