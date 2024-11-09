
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

interface Participant {
  name: string;
  email: string;
}

const route = useRoute();
const groupId = route.params.groupId as string;

const name = ref('');
const email = ref('');
const participants = ref<Participant[]>([]);

const addParticipant = async () => {
  const response = await fetch('/api/addParticipant', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ groupId, name: name.value, email: email.value })
  });
  const data = await response.json();
  if (data.message === 'Participant ajouté') {
    participants.value.push({ name: name.value, email: email.value });
    name.value = '';
    email.value = '';
  }
};

const generatePairs = async () => {
  const response = await fetch('/api/generatePairs', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ groupId })
  });
  const data = await response.json();
  alert('Paires générées : ' + JSON.stringify(data.pairs));
};
</script>

<template>
    <div>
      <h2>Groupe {{ groupId }}</h2>
      <form @submit.prevent="addParticipant">
        <input v-model="name" placeholder="Nom" />
        <input v-model="email" placeholder="Email" />
        <button type="submit">Ajouter Participant</button>
      </form>
      <button @click="generatePairs">Générer les paires</button>
      <ul>
        <li v-for="participant in participants" :key="participant.email">{{ participant.name }}</li>
      </ul>
    </div>
</template>