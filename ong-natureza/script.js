// Dados simulados da ONG
const impactData = {
    trees: 15420,
    co2Reduced: 2847,
    projects: 23,
    volunteers: 156
};

// Animação de contadores
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    const timer = setInterval(() => {
        start += increment;
        element.textContent = Math.floor(start).toLocaleString();
        
        if (start >= target) {
            element.textContent = target.toLocaleString();
            clearInterval(timer);
        }
    }, 16);
}

// Mostrar impacto em tempo real
function showImpact() {
    const impactDisplay = document.getElementById('impact-data');
    
    impactDisplay.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; text-align: center;">
            <div>
                <div style="font-size: 2rem; font-weight: bold;">${impactData.projects}</div>
                <div>Projetos Ativos</div>
            </div>
            <div>
                <div style="font-size: 2rem; font-weight: bold;">${impactData.volunteers}</div>
                <div>Voluntários</div>
            </div>
            <div>
                <div style="font-size: 2rem; font-weight: bold;">12</div>
                <div>Estados Atendidos</div>
            </div>
        </div>
        <p style="margin-top: 2rem; font-size: 1.1rem;">
            Nossos projetos já evitaram o desmatamento de 3.200 hectares de floresta nativa.
        </p>
    `;
    
    // Scroll suave para a seção
    document.getElementById('impact').scrollIntoView({ behavior: 'smooth' });
}

// Ações dos botões
function donate() {
    alert('🌱 Obrigado pelo interesse! Em breve teremos nossa plataforma de doações online.');
}

function volunteer() {
    alert('🤝 Que incrível! Entre em contato conosco: voluntarios@verdevivo.org');
}

function share() {
    if (navigator.share) {
        navigator.share({
            title: 'Verde Vivo ONG',
            text: 'Conheça a Verde Vivo - ONG que combate o desmatamento e reduz emissões de CO₂',
            url: window.location.href
        });
    } else {
        alert('🔗 Compartilhe nossa causa: ' + window.location.href);
    }
}

// Navegação suave
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Inicialização quando a página carrega
document.addEventListener('DOMContentLoaded', () => {
    // Animar contadores na hero
    setTimeout(() => {
        animateCounter(document.getElementById('trees'), impactData.trees);
        animateCounter(document.getElementById('co2'), impactData.co2Reduced);
    }, 500);
    
    // Efeito de parallax simples no scroll
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.1}px)`;
        }
    });
});
