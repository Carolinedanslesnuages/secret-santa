<script setup lang="ts">
  import { ref } from 'vue';
  
  const groupId = ref<string | null>(null);
  
  const createGroup = async () => {
    // Appel de l'API pour créer un groupe
    const response = await fetch('/api/createGroup', { method: 'POST' });
    const data = await response.json();
    groupId.value = data.groupId;
  };
  </script>

<template>
    <div>
      <h2>Créer un groupe Secret Santa</h2>
      <button @click="createGroup">Créer</button>
      <div v-if="groupId">ID de Groupe : {{ groupId }}</div>
    </div>
</template>