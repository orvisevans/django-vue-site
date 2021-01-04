<template>
  <div>
    <router-link :to="questionDetailUrl">
      <h3>{{ question.question_text }}</h3>
    </router-link>
    <p class="date">{{ question.pub_date }}</p>
  </div>
</template>

<script>
export default {
  name: "QuestionSummary",
  props: {
    question: Object,
  },
  computed: {
    questionDetailUrl() {
      return `/question/${this.question.id}`;
    },
  },
};
</script>

<style scoped>
</style>
