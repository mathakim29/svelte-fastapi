<script>
  let { navigate } = $props()
</script>

<main class="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
  <div class="mx-auto max-w-xl space-y-4">
    <button onclick={() => navigate('/')} class="text-cyan-400">← Home</button>
    <h1 class="text-3xl font-bold">About</h1>
    <p class="text-slate-400">Add your app screens here.</p>
  </div>
</main>
