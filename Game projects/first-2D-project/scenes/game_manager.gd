extends Node
@onready var score_label: Label = $ScoreLabel

var score=0

func add_point():
	score+=1
	if score<12:
		score_label.text="Score:"+str(score)
	else:
		score_label.text="perfection!"
	
