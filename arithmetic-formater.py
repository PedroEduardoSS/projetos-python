def arithmetic_arranger(problems, answer=False):
  l1 = ""
  l2 = ""
  l3 = ""
  l4 = ""

  test_too_many_problems = len(problems)
  if test_too_many_problems > 5:
    return "Error: Too many problems."

  for elem in problems:
    num1 = elem.split(" ")[0]
    oper = elem.split(" ")[1]
    num2 = elem.split(" ")[2]
    

    many_digits1 = len(num1)
    many_digits2 = len(num2)

    if many_digits1 > 4:
      return "Error: Numbers cannot be more than four digits."
    elif many_digits2 > 4:
      return "Error: Numbers cannot be more than four digits."

    try:
      if oper == "+":
        ans = int(num1) + int(num2)
      elif oper == "-":
        ans = int(num1) - int(num2)
      elif oper == "*":
          ans = int(num1) * int(num2)
      elif oper == "/":
          ans = int(num1) / int(num2)
    except:
      return "Error: Numbers must only contain digits."
    

    try:
      formatation = str(ans).strip("-")
    except:
      formatation = str(ans)
    underlines = "-" * (len(str(formatation)) + 2)

    line1 = num1.rjust(len(str(formatation)) + 2)
    line2 = oper + " " + num2.rjust(len(str(formatation)))
    line3 = underlines.rjust(len(str(formatation)) + 2)
    line4 = str(ans).rjust(len(str(formatation)) + 2)
    
    l1 += line1  + "   "
    l2 += line2  + "   "
    l3 += line3  + "   "
    l4 += line4  + "   "

  if answer:
    full_line = "\n" + l1 + "\n" + l2 + "\n" + l3 + "\n" + l4
    print(full_line)
  else:
    full_line = "\n" + l1 + "\n" + l2 + "\n" + l3 + "\n"
    print(full_line)
    
arithmetic_arranger(["40 + 50", "3 - 2", "10 * 6", "24 / 6"], True)