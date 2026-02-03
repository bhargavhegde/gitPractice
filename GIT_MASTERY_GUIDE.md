# Git Mastery Guide: Theory & Practice (3-Person Edition)

This guide is designed for **Bhargav**, **Rishab** (rishabds7), and **Pavithran** (pavithran2003) to master Git commands, workflows, and industry standards for your interview.

## Part 1: Essential Git Theory & Best Practices

### 1. The Three States
Git has three main states that your files can reside in:
- **Modified**: You have changed the file but have not committed it to your database yet.
- **Staged**: You have marked a modified file in its current version to go into your next commit snapshot.
- **Committed**: The data is safely stored in your local database.

> **💡 Best Practice: Atomic Commits**  
> Don't stage everything at once (`git add .`) if you worked on two unrelated features. Stage and commit them separately. Each commit should do **one** thing and do it well. This makes it easier to undo specific changes later.

### 2. Basic Concepts
- **Repository (Repo)**: A directory where Git stores all your files and their history.
- **Commit**: A snapshot of your repository at a specific point in time. Each commit has a unique ID (hash).
- **Branch**: A movable pointer to one of these commits. The default branch name is usually `main` or `master`.
- **HEAD**: A special pointer that points to the local branch you’re currently on.

> **💡 Best Practice: Commit Messages**  
> Use the **Imperative Mood** (command form).  
> *   ✅ Good: "Add login functionality"  
> *   ❌ Bad: "Added login functionality" or "I fixed the login bug"  
> *   Why? Git itself uses this style (e.g., "Merge branch 'feature'").

### 3. Merge vs. Rebase
This is a common interview topic.
- **Merge**: Combines two branches. It creates a new "merge commit" in the history. It preserves the history exactly as it happened.
    - *Pros*: Non-destructive, shows exactly when code was integrated.
    - *Cons*: History can become messy/cluttered with merge commits.
- **Rebase**: Moves the entire branch to begin on the tip of the `main` branch. It rewrites history to make it look linear.
    - *Pros*: Clean, linear history.
    - *Cons*: Dangerous if not used carefully on shared public branches.

> **💡 Best Practice: Golden Rule of Rebasing**  
> **NEVER rebase a branch that you have pushed to a public repository** if anyone else is working on it. Rebase is fine for your *local* feature branch before you push it to clean up history, but once shared, treat history as immutable.

### 4. Resolving Conflicts
Conflicts happen when two branches have changed the same part of the same file.

> **💡 Best Practice: Communication**  
> When a conflict occurs in a team, don't just guess! If you see Pavithran changed a line you also changed, and you aren't sure which version is correct, **talk to him**. "Winning" the conflict isn't the goal; correct code is.

### 5. Advanced Concepts
- **Cherry-pick**: Applying changes from a specific commit to your current branch.
- **Stash**: Temporarily shelves changes.
- **Reset vs Revert**: `reset` rewrites history (dangerous); `revert` adds a new "undo" commit (safe).

---

## Part 2: Practical Workshop Script (3-Person Simulation)

Follow these steps exactly in your terminal. We will use **branches** to simulate three people working on one machine.

**Assign Roles:**
1.  **Bhargav**: The Project Lead (Manages `main`, sets up repo).
2.  **Rishab**: Developer 1 (Works on core math features).
3.  **Pavithran**: Developer 2 (Works on advanced features & documentation).

### Phase 1: Setup (Bhargav)

> **💡 Best Practice: .gitignore**  
> Before writing any code, always set up a `.gitignore` file. This prevents junk files (like `__pycache__`, `.DS_Store`, or `node_modules`) from polluting the repo.

1.  **Initialize the Project**
    ```bash
    # (Clean up previous run if needed: rm -rf ~/Desktop/gitPractice)
    mkdir -p ~/Desktop/gitPractice
    cd ~/Desktop/gitPractice
    git init
    
    # Create .gitignore FIRST
    echo "__pycache__/" > .gitignore
    echo "*.log" >> .gitignore
    
    echo "# Git Practice Project" > README.md
    git add .
    git commit -m "Initial commit by Bhargav"
    ```

2.  **Create the base file**
    Bhargav creates `calculator.py`:
    ```python
    class Calculator:
        def __init__(self):
            print("Calculator initialized")
    ```
    
    Commit it:
    ```bash
    git add calculator.py
    git commit -m "Add Calculator class structure"
    ```

### Phase 2: Parallel Development (Rishab & Pavithran)

> **💡 Best Practice: Branch Naming Conventions**  
> Use descriptive prefixes:  
> *   `feature/` for new features  
> *   `bugfix/` or `fix/` for bug fixes  
> *   `hotfix/` for urgent production fixes  
> *   `chore/` for maintenance (updating deps, configs)

3.  **Rishab starts working (Feature: Basic Math)**
    ```bash
    git checkout main
    git checkout -b feature/rishab-basic-math
    ```
    
    Rishab adds Add/Subtract to `calculator.py`:
    ```python
    class Calculator:
        def __init__(self):
            print("Calculator initialized")

        def add(self, a, b):
            return a + b

        def subtract(self, a, b):
            return a - b
    ```
    
    Commit:
    ```bash
    git add calculator.py
    git commit -m "Add add and subtract methods"
    ```

4.  **Pavithran starts working (Feature: Advanced Math)**
    ```bash
    # Pavithran branches off main (NOT Rishab's branch)
    git checkout main
    git checkout -b feature/pavithran-adv-math
    ```
    
    Pavithran adds Multiply/Divide. 
    ```python
    class Calculator:
        def __init__(self):
            print("Scientific Calculator initialized") # Pavithran changes this line too!

        def multiply(self, a, b):
            return a * b

        def divide(self, a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
    ```
    
    Commit:
    ```bash
    git add calculator.py
    git commit -m "Add multiply and divide methods"
    ```

### Phase 3: The Merge & Conflict Resolution

> **💡 Best Practice: Pull Before Push**  
> Before merging, you should usually update your local main to ensure you aren't merging into an outdated version. (Simulated here by just checking out main).

5.  **Rishab merges his code first**
    Bhargav reviews Rishab's code and merges it into main.
    ```bash
    git checkout main
    git merge feature/rishab-basic-math
    # Fast-forward merge (success)
    ```

6.  **Pavithran tries to merge (Conflict Time!)**
    ```bash
    git checkout main
    git merge feature/pavithran-adv-math
    ```
    **Result:** `CONFLICT (content): Merge conflict in calculator.py`.

7.  **Pavithran Resolves the Conflict**
    Open `calculator.py`.
    
    > **💡 Best Practice: Verify before Committing**  
    > After resolving conflict markers (`<<<<`, `====`, `>>>>`), ALWAYS run the code (if possible) to make sure you didn't break the syntax.
    
    *Corrected Code:*
    ```python
    class Calculator:
        def __init__(self):
            print("Scientific Calculator initialized") 

        def add(self, a, b):
            return a + b

        def subtract(self, a, b):
            return a - b

        def multiply(self, a, b):
            return a * b

        def divide(self, a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
    ```
    
    Finish the merge:
    ```bash
    git add calculator.py
    git commit -m "Merge Pavithran's changes and resolve conflict"
    ```

### Phase 4: The "Rebase" Workflow (Keeping History Clean)

> **💡 Best Practice: Rebase for Updates**  
> If `main` has moved forward while you were working, don't just merge `main` into your branch (which creates a "merge bubble"). Instead, **rebase your feature branch on top of main**. This makes it look like you just started your work *after* the latest updates.

8.  **Bhargav makes a change on main**
    ```bash
    git checkout main
    echo "v1.0" > version.txt
    git add version.txt
    git commit -m "Release v1.0"
    ```

9.  **Rishab starts a new feature (Square Root)**
    ```bash
    git checkout -b feature/rishab-sqrt HEAD~1 
    # Rishab starts from an older commit
    ```
    
    Rishab works:
    ```bash
    echo "Square root logic" > sqrt_utils.py
    git add sqrt_utils.py
    git commit -m "Add sqrt logic"
    ```

10. **Rishab rebases to get the update**
    Rishab wants `version.txt` in his branch without creating a merge commit.
    ```bash
    git rebase main
    ```
    *Result*: History is now linear. Rishab's commit is placed *after* "Release v1.0".

### Phase 5: Cherry-Picking (The "Oops" Fix)

11. **Pavithran makes a mistake**
    ```bash
    git checkout -b pavithran-experiments
    echo "Experimental Code" > experiment.py
    git add experiment.py
    git commit -m "Add experiments"
    
    # The Fix
    echo "# Git Practice Project - OFFICIAL" > README.md
    git add README.md
    git commit -m "Fix typo in README title"
    ```

12. **Bhargav wants JUST the fix**
    > **💡 Best Practice: Don't Commit unrelated changes**  
    > If Pavithran had followed the Atomic Commit rule, this would be easy. Since the fix is in its own commit, we can cherry-pick it. If he had mixed the fix with the experiment code, we would be in trouble!

    ```bash
    git log --oneline
    # Copy the hash of "Fix typo in README title" (e.g., abc1234)
    ```
    
    Bhargav goes to main:
    ```bash
    git checkout main
    git cherry-pick <HASH_OF_FIX_TYPO_COMMIT>
    ```

### Phase 6: Interactive Rebase (Squashing History)

> **💡 Best Practice: Clean up before you Merge**  
> Your feature branch might have 10 commits like "wip", "typo", "fix". Nobody needs to see that in the main history. **Squash** them into one clean commit before merging.

13. **Rishab creates messy commits**
    ```bash
    git checkout -b feature/rishab-messy
    touch temp1.txt; git add .; git commit -m "wip 1"
    touch temp2.txt; git add .; git commit -m "wip 2"
    touch temp3.txt; git add .; git commit -m "done"
    ```

14. **Squashing them into one**
    ```bash
    git rebase -i HEAD~3
    ```
    - Change `pick` to `squash` (or `s`) for the 2nd and 3rd commits.
    - Rename the final commit message to "Add temp files feature complete".

### Phase 7: Emergency Undo & Safety

> **💡 Best Practice: Never force push to main**  
> `git push --force` destroys history on the remote server. If you must fix a public branch, use `git revert` or `git push --force-with-lease` (which checks if anyone else pushed recently).

15. **Stashing**
    > **💡 Best Practice: Don't commit broken code just to switch branches**  
    > Use stash instead.
    
    ```bash
    git checkout main
    echo "Unfinished work..." >> version.txt
    git stash
    git checkout feature/rishab-messy # Success!
    git checkout main
    git stash pop
    ```

16. **Reset (The "Nuke" Option)**
    ```bash
    git reset --hard HEAD~1
    ```

---
**Summary of Best Practices:**
1.  **Commit Often, Perfect Later**: Commit frequently locally, but squash/clean up before sharing.
2.  **Write Good Messages**: Imperative mood, explain *why* not just *what*.
3.  **Pull/Rebase Frequently**: Keep your branch up to date with `main` to avoid massive conflicts at the end.
4.  **Use Branches**: Never work directly on `main`.
5.  **Review Code**: In a real team, always use Pull Requests (PRs) instead of merging directly.

Good luck Bhargav, Rishab, and Pavithran!
