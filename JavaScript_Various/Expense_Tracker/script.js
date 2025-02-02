// Wait until the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", function () {
  // --- Add the function ad event listener to toggle the visibility of the Expense Form. That will be shown only on the button click.
  //
  // Select the "Add Expense" button
  const addExpenseBtn = document.querySelector(".add-expense-btn");
  // Select the expense form that needs to be shown/hidden
  const expenseForm = document.querySelector(".expense-form");
  // AddExpenseBtn is a variable that store a reference to the "Add Expense" button in the HTML
  addExpenseBtn.addEventListener("click", function () {
    // Get the computed style of the expense form
    const computedStyle = getComputedStyle(expenseForm);
    // Check the current display state of the expense form
    if (
      computedStyle.display === "none" ||
      expenseForm.style.display === "none"
    ) {
      // If the form is hidden or has no inline display style, show it
      expenseForm.style.display = "block";
    } else {
      // Otherwise, hide the form
      expenseForm.style.display = "none";
    }
  });

  // --- Select the checkboxes
  //
  // Select the checkboxes element for including or nor including in previous expenses
  const includePreviousCheckbox = document.getElementById("include-previous");
  const notIncludePreviousCheckbox = document.getElementById("not-include-previous");
  // Function to ensure that at least one checkbox is always checked.
  function ensureOneChecked() {
    // If both the checkboxes are unchecked, by default check the "Include previous expenses" checkbox by default.
    if (
      !includePreviousCheckbox.checked &&
      !notIncludePreviousCheckbox.checked
    ) {
      includePreviousCheckbox.checked = true;
    }
  }

  // Add event listener to the "Include in Previous Expenses" checkbox. The 'change' event is triggered when the value of an input element changes.
  includePreviousCheckbox.addEventListener("change", function () {
    if (includePreviousCheckbox.checked) {
      // If this checkbox is checked, uncheck the other one
      notIncludePreviousCheckbox.checked = false;
    } else {
      // If this checkbox is unchecked, recheck it, to ensure that one checkbox is always checked.
      includePreviousCheckbox.checked = true;
    }
  });
  // Add event listener to the "Not include in previous Expenses" checkbox
  notIncludePreviousCheckbox.addEventListener("change", function () {
    if (notIncludePreviousCheckbox.checked) {
      // If this checkbox is checked, uncheck the other one
      includePreviousCheckbox.checked = false;
    } else {
      // If this checkbox is unchecked, recheck it to ensure that one checkbox is always checked.
      notIncludePreviousCheckbox.checked = true;
    }
  });
  // Ensure that at least one checkbox is checked on page load
  ensureOneChecked();

  // --- Add the function to hide and show the add participant form on button click
  //
  // Here I cannot use the getElementById(), because the element in the HTML does not have any ID associated to it. I could simply used it, by defining the id="" to the HTML elements. 
  // Retrieve the add participant button
  const addParticipantBtn = document.querySelector(".add-participant-btn");
  // Retrieve the add participant form
  const addParticipantForm = document.querySelector(".add-participant-form");
  // Add the EventListener at the click of the Add Participant Button
  addParticipantBtn.addEventListener("click", function () {
    // Check if the addParticipantForm display visibility is none, if it is set it to block, and vice versa.
    // - getComputedStyle, which is a function used to get the computed style properties of an element. The computed style is the final set of CSS properties that are applied to an element after all stylesheets, style attributes, and any other CSS rule have been applied.
    const computedStyleForm = getComputedStyle(addParticipantForm);
    // Check if the form is showing or not.
    if (
      computedStyleForm.display === "none" ||
      addParticipantForm.style.display === "none"
    ) {
      addParticipantForm.style.display = "block";
    } else {
      addParticipantForm.style.display = "none";
    }
  });

  // --- Handle the participant form submission to add the new participant
  // 
  // Retrieve the Add participant button. 
  const submitParticipantBtn = document.getElementById("add-participant-form");
  // Add the Event Listener to this submit form button
  submitParticipantBtn.addEventListener('click', function(event){
    // Prevent the default form submission
    event.preventDefault();
    
    // Get the input element for the participant name
    const newParticipantNameInput = document.querySelector("#participant-name");
    // Get the trimmed (without white spaces) of the participant name
    const newParticipantName = newParticipantNameInput.value.trim();

    // Check if the participant name is not empty
    if (newParticipantName){
      // Get the participants list elements
      const participantsList = document.querySelector(".participants-list");
      // Create a new list item element.
      const listItem = document.createElement("li");
      // Set the text content of the list item to the new participant name. 
      listItem.textContent = newParticipantName;
      // Append the new list item to the participant list. 
      participantsList.append(listItem);

      // TO BE COMPLETED !!! Asking for defining different styling for the new list element, as well as adding the info about what they own to who.
    }
  });
});
