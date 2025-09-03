import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import ReviewView from '../views/ReviewView.vue'
import LibraryView from '../views/LibraryView.vue'
import StatsView from '../views/StatsView.vue'
import ImportView from '../views/ImportView.vue'
import CardView from '../views/CardView.vue'

const routes: RouteRecordRaw[] = [
  { path: '/login', component: LoginView },
  { path: '/review', component: ReviewView },
  { path: '/cards/:id', component: CardView },
  { path: '/library', component: LibraryView },
  { path: '/stats', component: StatsView },
  { path: '/import', component: ImportView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
