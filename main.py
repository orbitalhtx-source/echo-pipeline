
{/* Toast notification */}
{toast && <div className="toast">{toast}</div>}
</div>
);
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<CoinverseApp />);
</script>

<!-- Service Worker for PWA (offline support) -->
<script>
if ('serviceWorker' in navigator) {
window.addEventListener('load', () => {
navigator.serviceWorker.register(
URL.createObjectURL(
new Blob([`
const CACHE = 'coinverse-v1';
self.addEventListener('install', e => {
e.waitUntil(
caches.open(CACHE).then(cache =>
cache.addAll(['./'])
)
);
});
self.addEventListener('fetch', e => {
e.respondWith(
caches.match(e.request).then(resp =>
resp || fetch(e.request).then(response => {
if(response.ok) {
const clone = response.clone();
caches.open(CACHE).then(cache => cache.put(e.request, clone));
}
return response;
})
)
);
});
`], { type: 'application/javascript' })
)
);
});
}
</script>


</body>
</html>
