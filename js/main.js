// =====================================================
// 借金6億ニキ公式メディア - メインJavaScript
// =====================================================

document.addEventListener('DOMContentLoaded', function() {
    
    // =====================================================
    // ナビゲーション関連
    // =====================================================
    const navbar = document.querySelector('.main-header');
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // スクロール時のヘッダー背景変更
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.background = 'rgba(0, 26, 77, 0.98)';
            navbar.style.backdropFilter = 'blur(15px)';
        } else {
            navbar.style.background = 'rgba(0, 26, 77, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        }
        
        // スクロール方向によるヘッダーの表示/非表示
        if (currentScroll > lastScroll && currentScroll > 500) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
    
    // ハンバーガーメニューのトグル
    if (hamburger) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // モバイルメニュー用のスタイルを動的に追加
            if (navMenu.classList.contains('active')) {
                navMenu.style.display = 'flex';
                navMenu.style.position = 'fixed';
                navMenu.style.flexDirection = 'column';
                navMenu.style.top = '70px';
                navMenu.style.left = '0';
                navMenu.style.width = '100%';
                navMenu.style.background = 'rgba(0, 26, 77, 0.98)';
                navMenu.style.padding = '2rem';
                navMenu.style.gap = '1rem';
                navMenu.style.zIndex = '999';
                navMenu.style.animation = 'slideDown 0.3s ease';
            } else {
                setTimeout(() => {
                    navMenu.style.display = '';
                    navMenu.style.position = '';
                    navMenu.style.flexDirection = '';
                    navMenu.style.top = '';
                    navMenu.style.left = '';
                    navMenu.style.width = '';
                    navMenu.style.background = '';
                    navMenu.style.padding = '';
                }, 300);
            }
        });
    }
    
    // スムーススクロール
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                    
                    // アクティブクラスの更新
                    navLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                    
                    // モバイルメニューを閉じる
                    if (navMenu.classList.contains('active')) {
                        hamburger.click();
                    }
                }
            }
        });
    });
    
    // =====================================================
    // セクション監視とアクティブリンク更新
    // =====================================================
    const sections = document.querySelectorAll('section[id]');
    const observerOptions = {
        rootMargin: '-100px 0px -100px 0px',
        threshold: 0.3
    };
    
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        sectionObserver.observe(section);
    });
    
    // =====================================================
    // ヒーローセクションのパーティクル効果
    // =====================================================
    const particleField = document.querySelector('.particle-field');
    if (particleField) {
        const createParticle = () => {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.cssText = `
                position: absolute;
                width: ${Math.random() * 4 + 1}px;
                height: ${Math.random() * 4 + 1}px;
                background: rgba(0, 212, 255, ${Math.random() * 0.5 + 0.2});
                border-radius: 50%;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                animation: float ${Math.random() * 10 + 10}s linear infinite;
                box-shadow: 0 0 ${Math.random() * 10 + 5}px rgba(0, 212, 255, 0.5);
            `;
            particleField.appendChild(particle);
            
            // パーティクルの削除
            setTimeout(() => {
                particle.remove();
            }, 20000);
        };
        
        // 初期パーティクル生成
        for (let i = 0; i < 30; i++) {
            setTimeout(createParticle, i * 100);
        }
        
        // 継続的なパーティクル生成
        setInterval(createParticle, 1000);
    }
    
    // =====================================================
    // カウントアップアニメーション
    // =====================================================
    const animateValue = (element, start, end, duration) => {
        const startTimestamp = Date.now();
        const step = () => {
            const timestamp = Date.now();
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const value = Math.floor(progress * (end - start) + start);
            
            if (element.dataset.suffix) {
                element.textContent = value + element.dataset.suffix;
            } else {
                element.textContent = value.toLocaleString();
            }
            
            if (progress < 1) {
                requestAnimationFrame(step);
            }
        };
        requestAnimationFrame(step);
    };
    
    // 統計カードのアニメーション
    const statNumbers = document.querySelectorAll('.stat-number.animated');
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                entry.target.classList.add('counted');
                const value = parseInt(entry.target.textContent);
                const suffix = entry.target.dataset.suffix || '';
                
                if (suffix === '億') {
                    animateValue(entry.target, 0, 6, 2000);
                } else if (value === 6000 && suffix === '+') {
                    animateValue(entry.target, 0, 6000, 2000);
                } else if (value === 500 && suffix === '+') {
                    animateValue(entry.target, 0, 500, 2000);
                }
            }
        });
    }, { threshold: 0.5 });
    
    statNumbers.forEach(stat => {
        statsObserver.observe(stat);
    });
    
    // =====================================================
    // ニュースレター登録フォーム
    // =====================================================
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const emailInput = newsletterForm.querySelector('input[type="email"]');
            const submitButton = newsletterForm.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            // ボタンをローディング状態に
            submitButton.disabled = true;
            submitButton.textContent = '送信中...';
            submitButton.style.opacity = '0.7';
            
            // ここで実際のAPI呼び出しを行う
            try {
                // 仮の遅延（実際のAPI呼び出しに置き換える）
                await new Promise(resolve => setTimeout(resolve, 2000));
                
                // 成功時の処理
                submitButton.textContent = '✓ 登録完了！';
                submitButton.style.background = 'linear-gradient(135deg, #00ff88 0%, #00d455 100%)';
                
                // 入力フィールドをクリア
                emailInput.value = '';
                
                // 3秒後に元に戻す
                setTimeout(() => {
                    submitButton.disabled = false;
                    submitButton.textContent = originalText;
                    submitButton.style.background = '';
                    submitButton.style.opacity = '';
                }, 3000);
                
                // 成功通知を表示
                showNotification('メルマガ登録ありがとうございます！', 'success');
                
            } catch (error) {
                // エラー時の処理
                submitButton.disabled = false;
                submitButton.textContent = originalText;
                submitButton.style.opacity = '';
                showNotification('登録に失敗しました。もう一度お試しください。', 'error');
            }
        });
    }
    
    // =====================================================
    // 通知表示機能
    // =====================================================
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            padding: 1rem 2rem;
            background: ${type === 'success' ? 'linear-gradient(135deg, #00ff88 0%, #00d455 100%)' : 
                         type === 'error' ? 'linear-gradient(135deg, #ff3b30 0%, #ff6b6b 100%)' : 
                         'linear-gradient(135deg, #0066ff 0%, #00d4ff 100%)'};
            color: white;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            animation: slideInRight 0.3s ease;
            font-weight: 600;
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // 3秒後に削除
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
    
    // =====================================================
    // 記事カードのホバーエフェクト
    // =====================================================
    const articleCards = document.querySelectorAll('.article-card');
    articleCards.forEach(card => {
        card.addEventListener('mouseenter', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const glow = document.createElement('div');
            glow.className = 'card-glow';
            glow.style.cssText = `
                position: absolute;
                top: ${y}px;
                left: ${x}px;
                width: 100px;
                height: 100px;
                background: radial-gradient(circle, rgba(0, 212, 255, 0.4) 0%, transparent 70%);
                border-radius: 50%;
                transform: translate(-50%, -50%);
                pointer-events: none;
                animation: glowExpand 0.5s ease;
            `;
            
            card.style.position = 'relative';
            card.appendChild(glow);
            
            setTimeout(() => glow.remove(), 500);
        });
    });
    
    // =====================================================
    // タイムラインアニメーション
    // =====================================================
    const timelineItems = document.querySelectorAll('.timeline-item');
    const timelineObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                setTimeout(() => {
                    entry.target.classList.add('animated');
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateX(-50px)';
                    entry.target.style.animation = 'slideInLeft 0.6s ease forwards';
                }, index * 100);
            }
        });
    }, { threshold: 0.3 });
    
    timelineItems.forEach(item => {
        timelineObserver.observe(item);
    });

    // =====================================================
    // 画像の遅延読み込み
    // =====================================================
    const lazyImages = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    }, { rootMargin: '50px' });
    
    lazyImages.forEach(img => {
        imageObserver.observe(img);
    });
});

// =====================================================
// CSSアニメーション用のスタイル追加
// =====================================================
const style = document.createElement('style');
style.textContent = `
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideOutRight {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100px);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes float {
        0% {
            transform: translateY(0) translateX(0);
        }
        33% {
            transform: translateY(-30px) translateX(30px);
        }
        66% {
            transform: translateY(30px) translateX(-30px);
        }
        100% {
            transform: translateY(0) translateX(0);
        }
    }
    
    @keyframes glowExpand {
        0% {
            width: 0;
            height: 0;
            opacity: 1;
        }
        100% {
            width: 200px;
            height: 200px;
            opacity: 0;
        }
    }
    
    .hamburger.active span:nth-child(1) {
        transform: rotate(45deg) translate(5px, 5px);
    }
    
    .hamburger.active span:nth-child(2) {
        opacity: 0;
    }
    
    .hamburger.active span:nth-child(3) {
        transform: rotate(-45deg) translate(7px, -6px);
    }
`;
document.head.appendChild(style);