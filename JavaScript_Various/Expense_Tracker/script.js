// Wait until the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", function () {
  // Get the add Expense button.
  const addExpenseBtn = document.querySelector(".add-expense-btn");
  // Select the expense form that needs to be shown/hidden
  const expenseForm = document.querySelector(".expense-form");
  // Select the checkboxes element for including or nor including in previous expenses
  const includePreviousCheckbox = document.getElementById("include-previous");
  const notIncludePreviousCheckbox = document.getElementById(
    "not-include-previous"
  );
  // Here I cannot use the getElementById(), because the element in the HTML does not have any ID associated to it. I could simply used it, by defining the id="" to the HTML elements.
  // Retrieve the add participant button
  const addParticipantBtn = document.querySelector(".add-participant-btn");
  // Retrieve the add participant form
  const addParticipantForm = document.querySelector(".add-participant-form");
  // Retrieve the Add participant button.
  const submitParticipantBtn = document.getElementById("add-participant-form");
  // Retrieve the clear participant button.
  const clearParticipantBtn = document.getElementById("clear-participant-form");
  // Get the participants list elements
  const participantsList = document.querySelector(".participants-list");
  // Retrieve the PaidBy container
  const paidByContainer = document.getElementById("payerCheckboxes");
  // Retrieve the SplitBy container
  const splitByContainer = document.getElementById("splitCheckboxes");
  // Retrieve the add expense form submit/add button
  const submitExpenseBtn = document.getElementById("add-expense-form");
  // Retrieve the expense history
  const expenseHistoryList = document.querySelector(".expense-history");

  // Fake some data expenses
  const expenses = [
    { participant: "Pippo", amount: 300 },
    { participant: "Pluto", amount: 300 },
  ];

  // --- Select the checkboxes
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

  // --- Function used to update the "Paid By" and "Split By" sections
  function updateExpenseFormParticipants() {
    // Get the array of participant names from the list items
    const participants = Array.from(participantsList.children).map((li) =>
      li.textContent.trim()
    );

    // Clear existing participants in the "Paid By" and "Split By" section
    paidByContainer.innerHTML = "";
    splitByContainer.innerHTML = "";

    // Loop through all the participant in the participants array
    participants.forEach((participant, index) => {
      // Create "Paid By" radio button
      const paidByLabel = document.createElement("label");
      const paidByRadio = document.createElement("input");
      paidByRadio.type = "radio";
      paidByRadio.name = "paid-by"; // Ensure only one radio button can be selected.
      paidByRadio.value = participant;
      // By default check the first participant as the one that paid
      if (index === 0) {
        paidByRadio.checked = true;
      }
      paidByLabel.appendChild(paidByRadio);
      paidByLabel.appendChild(document.createTextNode(participant));
      paidByContainer.appendChild(paidByLabel);

      // Create "Split By" checkbox
      const splitByLabel = document.createElement("label");
      const splitByCheckbox = document.createElement("input");
      splitByCheckbox.type = "checkbox";
      splitByCheckbox.name = "split-by"; // Allow multiple checkboxes to be selected
      splitByCheckbox.value = participant;
      // Check by default to split by all. Check all the participants
      splitByCheckbox.checked = true;
      splitByLabel.appendChild(splitByCheckbox);
      splitByLabel.appendChild(document.createTextNode(participant));
      splitByContainer.appendChild(splitByLabel);
    });
  }

  // --- Add the function ad event listener to toggle the visibility of the Expense Form. That will be shown only on the button click.
  //
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
      // Access to the innerHTML
      addExpenseBtn.innerHTML =
        'Add Expense <i class="fa-solid fa-chevron-up"></i>';
    } else {
      // Otherwise, hide the form
      expenseForm.style.display = "none";
      addExpenseBtn.innerHTML =
        'Add Expense <i class="fa-solid fa-chevron-down"></i>';
    }
  });

  // --- Add event listener to the "Include in Previous Expenses" checkbox. The 'change' event is triggered when the value of an input element changes.
  includePreviousCheckbox.addEventListener("change", function () {
    if (includePreviousCheckbox.checked) {
      // If this checkbox is checked, uncheck the other one
      notIncludePreviousCheckbox.checked = false;
    } else {
      // If this checkbox is unchecked, recheck it, to ensure that one checkbox is always checked.
      includePreviousCheckbox.checked = true;
    }
  });
  // --- Add event listener to the "Not include in previous Expenses" checkbox
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
      // If it is not showing, then show it.
      addParticipantForm.style.display = "block";
      // Also change the "+" symbol on the button, to become a "-"
      // Access to the innerHTML
      addParticipantBtn.innerHTML =
        'Add Participant <i class="fa-solid fa-chevron-up"></i>';
    } else {
      addParticipantForm.style.display = "none";
      // Also change the symbol "-" to "+"
      addParticipantBtn.innerHTML =
        'Add Participant <i class="fa-solid fa-chevron-down"></i>';
    }
  });

  // --- Handle the participant form submission to add the new participant
  //
  // Add the Event Listener to this submit form button
  submitParticipantBtn.addEventListener("click", function (event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get the input element for the participant name
    const newParticipantNameInput = document.querySelector("#participant-name");
    // Get the trimmed (without white spaces) of the participant name
    const newParticipantName = newParticipantNameInput.value.trim();

    // Check if the participant name is not empty
    if (newParticipantName) {
      // Check if the number of participant, does not exceed 8.
      // If it exceeds 8, then set the stile of the Participants list to overflow-y: auto. It it goes over 15 alert the user that he has reached the maximum number of participant.
      // Get tne number of participants (length of the participants list)
      const numberOfParticipants = participantsList.children.length;
      const triggeringOverflow = 5;
      const maxParticipants = 15;
      if (
        numberOfParticipants > triggeringOverflow &&
        numberOfParticipants <= maxParticipants
      ) {
        // Get the participants-recap <div>
        const participantRecap = document.querySelector(".participants-recap");
        // Set the overflow-y property to the participantList
        // Retrieve the current height of the participant-recap element
        const participantRecapHeight = participantRecap.clientHeight;
        // Set its max height to the current height.
        participantRecap.style.maxHeight = `${participantRecapHeight}px`;
        // Set its overflow-Y to true.
        participantsList.style.overflowY = "scroll";
      } else if (numberOfParticipants > 8) {
        alert("Maximum number of participant already reached");
        // Get the Clear button element and trigger the click simulation
        const clearParticipantFormBtn = document.getElementById(
          "clear-participant-form"
        );
        // Trigger the clear button click action
        clearParticipantFormBtn.click();
        // Return in order not to add the participant.
        return;
      }

      // Create a new list item element.
      const listItem = document.createElement("li");
      // Set the text content of the list item to the new participant name.
      listItem.textContent = newParticipantName;
      // Append the new list item to the participant list.
      participantsList.appendChild(listItem);

      // Autoscroll to the last participant added
      listItem.scrollIntoView({ behavior: "smooth", block: "end" });

      // Clear the form field once submitted.
      newParticipantNameInput.value = "";
      includePreviousCheckbox.checked = false;
      notIncludePreviousCheckbox.checked = false;
      // Ensure one checkbox is always checked
      ensureOneChecked();

      // TO BE COMPLETED !!! Asking for defining different styling for the new list element, as well as adding the info about what they own to who.

      // --- Call the updateExpenseFormParticipants whenever a new participant is added to the participantsList
      updateExpenseFormParticipants();
    } else {
      // Alert the user if the participant name is empty
      alert("Please enter a Participant Name");
    }
  });

  // --- Handle the clear button to reset the form
  //
  // Add the event to the Clear participant button.
  clearParticipantBtn.addEventListener("click", function () {
    // Clear the participant name input field
    document.querySelector("#participant-name").value = "";
    // Uncheck both checkboxes
    includePreviousCheckbox.checked = false;
    notIncludePreviousCheckbox.checked = false;
    // Ensure one checkbox is checked.
    ensureOneChecked();
  });

  // --- Handle the add expense form
  submitExpenseBtn.addEventListener("click", function (event) {
    // Prevent the default form submission
    event.preventDefault();
    // Retrieve all the information added in the expense form. Description - Amount - Paid by - Split By
    const expenseDescription = document.getElementById("description").value;
    const expenseAmount = parseFloat(document.getElementById("amount").value);
    const expensePaidBy = document.getElementById("payerCheckboxes");
    // Loop through all the expensePaidBy and retrieve the checked element
    
    const expenseSplitBy = document.getElementById("splitCheckboxes");
  });
});
