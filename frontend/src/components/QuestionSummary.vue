<template>
  <div>
    <h3>{{ question.question_text }}</h3>
    <p class="date">{{ question.pub_date }}</p>
    <ul>
      <li v-for="choice in question.choices" :key="choice.id">
        {{ choice.choice_text }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "QuestionSummary",
  props: {
    question: Object,
  },
};
</script>

<style scoped>
</style>
