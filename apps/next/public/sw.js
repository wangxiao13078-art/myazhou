// Service Worker for PWA
const CACHE_NAME = 'math-quiz-v1';
const BASE_PATH = '/myazhou';

// 需要缓存的资源
const urlsToCache = [
  `${BASE_PATH}/`,
  `${BASE_PATH}/index.html`,
];

// 安装事件 - 缓存核心资源
self.addEventListener('install', (event) => {
  console.log('Service Worker: Installing...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Service Worker: Caching files');
        return cache.addAll(urlsToCache);
      })
      .then(() => self.skipWaiting())
  );
});

// 激活事件 - 清理旧缓存
self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activating...');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Service Worker: Clearing old cache');
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// 请求拦截 - 网络优先，失败时使用缓存
self.addEventListener('fetch', (event) => {
  // 只处理同源请求
  if (!event.request.url.startsWith(self.location.origin)) {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // 克隆响应用于缓存
        const responseClone = response.clone();
        
        // 缓存成功的 GET 请求
        if (event.request.method === 'GET' && response.status === 200) {
          caches.open(CACHE_NAME)
            .then((cache) => {
              cache.put(event.request, responseClone);
            });
        }
        
        return response;
      })
      .catch(() => {
        // 网络失败时从缓存获取
        return caches.match(event.request)
          .then((response) => {
            if (response) {
              return response;
            }
            // 如果是导航请求，返回首页
            if (event.request.mode === 'navigate') {
              return caches.match(`${BASE_PATH}/`);
            }
          });
      })
  );
});

