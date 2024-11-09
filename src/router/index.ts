import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'
import CreateGroup from '../views/CreateGroup.vue'
import Group from '../views/Group.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/create', name: 'CreateGroup', component: CreateGroup },
  { path: '/group/:groupId', name: 'Group', component: Group, props: true }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;