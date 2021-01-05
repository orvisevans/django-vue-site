<template>
  <div v-if="questionLoaded">
    <h3>{{ question.question_text }}: Results</h3>
    <p class="date">{{ question.pub_date }}</p>
    <ul>
      <li v-for="choice in question.choices" :key="choice.id">
        {{ choice.votes }}: {{ choice.choice_text }}
      </li>
    </ul>
  </div>
  <div v-else>
    <h3>Loading Question....</h3>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "QuestionSummary",
  data() {
    return {
      question: false,
    };
  },
  created() {
    axios
      .get(this.questionUrl)
      .then((response) => {
        const question = response.data;
        this.question = this.sortChoices(question);
      })
      .catch((err) => console.error(err));
  },
  computed: {
    questionLoaded() {
      return Boolean(this.question);
    },
    questionUrl() {
      const id = this.$route.params.id;
      return `http://localhost:8000/polls/api/questions/${id}?expand=choices`;
    },
  },
  methods: {
    sortChoices(question) {
      const sorted_choices = question.choices.sort((a, b) => b.votes - a.votes);
      return {
        ...question,
        choices: sorted_choices,
      };
    },
  },
};
</script>

<style scoped>
</style>
