<script>
  let { navigate } = $props()
  let result = ''

  async function checkApi() {
    const response = await fetch('/api/health')
    result = response.ok ? (await response.json()).message : 'API unavailable'
  }
</script>

<main class="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
  <div class="mx-auto max-w-xl space-y-6">
    <p class="text-sm font-semibold uppercase tracking-widest text-cyan-400">Svelte + FastAPI</p>
    <h1 class="text-4xl font-bold">Simple starter</h1>
    <p class="text-slate-400">A tiny Svelte frontend with a FastAPI backend.</p>
    <div class="flex gap-3">
      <button onclick={checkApi} class="rounded-lg bg-cyan-500 px-4 py-2 font-semibold text-slate-950">Check API</button>
      <button onclick={() => navigate('/about')} class="rounded-lg border border-slate-700 px-4 py-2">About</button>
    </div>
    {#if result}<p class="rounded-lg bg-slate-900 p-3 text-cyan-300">{result}</p>{/if}
  </div>
</main>
