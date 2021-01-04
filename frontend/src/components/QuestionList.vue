<template>
  <ul>
    <li v-for="question in questions" :key="question.id">
      <question-summary :question="question" />
    </li>
  </ul>
</template>

<script>
import QuestionSummary from "./QuestionSummary";
import axios from "axios";

export default {
  name: "QuestionList",
  components: {
    QuestionSummary,
  },
  async created() {
    if (this.questions.length !== 0) return;
    try {
      const url =
        "http://localhost:8000/polls/api/questions?expand=choices&format=json";
      const response = await axios.get(url);
      const { data } = response;
      this.questions = data;
    } catch (err) {
      console.err(err);
    }
  },
  data() {
    return {
      questions: [],
    };
  },
};
</script>

<style scoped>
</style>
