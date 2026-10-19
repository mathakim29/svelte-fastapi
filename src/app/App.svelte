<script>
  import { onMount } from 'svelte'
  import Home from './Home.svelte'
  import About from './About.svelte'

  let path = $state(window.location.pathname)
  const navigate = (next) => { history.pushState({}, '', next); path = next }
  onMount(() => { const update = () => path = window.location.pathname; addEventListener('popstate', update); return () => removeEventListener('popstate', update) })
</script>

{#if path === '/about'}
<About {navigate} />
{:else}
<Home {navigate} />
{/if}
