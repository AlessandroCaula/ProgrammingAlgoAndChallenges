// Wait until the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", function () {
  
  // Add the function ad event listener to toggle the visibility of the Expense Form. That will be shown only on the button click.
  // 
  // Select the "Add Expense" button
  const addExpenseBtn = document.querySelector(".add-expense-btn");
  // Select the expense form that needs to be shown/hidden
  const expenseForm = document.querySelector(".expense-form");
  // AddExpenseBtn is a variable that store a reference to the "Add Expense" button in the HTML
  addExpenseBtn.addEventListener("click", function() {
    // Get the computed style of the expense form
    const computedStyle = getComputedStyle(expenseForm);

    // Check the current display state of the expense form
    if (computedStyle.display === "none" || expenseForm.style.display === "none")
    {
      // If the form is hidden or has no inline display style, show it
      expenseForm.style.display = "block";
    } else {
      // Otherwise, hide the form
      expenseForm.style.display = "none";
    }
  });

  // Select the checkboxes
  // 
  // Select the checkboxes element for including or nor including in previous expenses
  const includePreviousCheckbox = document.getElementById('include-previous');
  const notIncludePreviousCheckbox = document.getElementById('not-include-previous');
});

