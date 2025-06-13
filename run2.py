from get_epics_ready_for_content import check_for_completion
from fetch_news import fetch_news_head
from gen_content import gen_post
from patch_post import fix_post


def loop(content):
    print("------ Generated LinkedIn Post ------")
    print(content)
    print("-------------------------------------")
    approval = input("Do you approve this post? (y/n): ")

    if approval.lower() == 'y':
        print("Post approved! Saving for publishing.")
        print("------ Generated LinkedIn Post ------")
        print(content)
        print("-------------------------------------")
        # Save to file or dashboard here
    elif approval.lower() == 'n':
        print("Post rejected. Please revise or discard.")
        feedback=input("please give your feedback or remark for the given content--")
        content=fix_post(content,feedback)
        loop(content)
        # You can implement editing or feedback here
    else:
        print("Invalid input. Please enter 'y' or 'n'.")



project = check_for_completion()
#print(type(project))
headline = fetch_news_head(project)
content= gen_post(project,headline)
loop(content)

