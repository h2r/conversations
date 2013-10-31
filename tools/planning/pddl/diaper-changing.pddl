; Note: this isn't proper pddl syntax.  I've changed a few things.  Namely, type hierarchy is now declared
; as (:types A B B.i B.ii C) in this example, there is a type B which has subtypes i and ii.  Also, there are now
; two more boolean operators forall, and exists that function as follows
;
; (forall ?x - type (function ?x)) = (and (function t1) (function t2) (function t3) ... ) where tn are of type "type"
; (exists ?x - type (function ?x)) = (or (function t1) (function t2) (function t3) ... ) where tn are of type "type"
;
; My PDDL extension also allows for constants, which are a set of objects that ALL instances of this domain must have

(:domain diaper-changing)

(:types location state contingency manipulator physobj physobj.old-clothing physobj.new-clothing human robot)

(:constants 
	Baby - human 
	Caregiver - human manipulator
	Robot - robot
	ChangingTable - location
	SideTable - location
	Hamper - location
	Dresser - location
	TrashCan - location
	OldDiaper - physobj
	NewDiaper - physobj
	StateX - state StateA - state
	StateB - state StateC - state
	StateD - state StateE - state
	StateF - state StateG - state)

(:predicates
	(arm ?x) (holdable ?obj) (holding ?arm ?obj) (empty ?arm) (at ?loc ?obj)
	(needs ?cont ?obj) (completed ?s) (resolved ?cont) (equals ?s1 ?s2))

(:action pick-up
	:parameters (?h - manipulator ?o - physobj ?l location)
	:precondition (and (arm ?h) (holding ?h ?o) (holdable ?o) (at ?l Robot) (at ?l ?o))
	:effect (and (holding ?h ?o) (not (empty ?h)) (not (at ?l ?o))))

(:action put-down
	:parameters (?h - manipulator ?o - physobj ?l - location)
	:precondition (and (arm ?h) (holding ?h ?o) (holdable ?o) (at Robot ?l))
	:effect (and (not (holding ?h ?o)) (at ?l ?o)))

(:action move
	:parameters (?l1 - location ?l2 - location)
	:precondition (at Robot ?l1)
	:effect (and (at Robot ?l2) (not (at Robot ?l1))))

(:action complete-state
	:parameters (?s - state)
	:precondition
		(and
			(forall ?c - contingency (resolved c))
			(or
				(equals ?s StateX)
				(and (equals ?s StateA)
					 (at ChangingTable Baby)
					 (completed StateX))
				(and (equals ?s StateB)
					 (forall ?c - physobj.old-clothing (at Hamper ?c))
					 (completed StateA))
				(and (equals ?s StateC)
					 (at OldDiaper TrashCan)
					 (completed StateB))
				(and (equals ?s StateD)
					 (completed StateC))
				(and (equals ?s StateE)
					 (at ChangingTable NewDiaper)
					 (completed StateD))
				(and (equals ?s StateF)
					 (forall ?c - physobj.new-clothing (at ChangingTable ?c))
					 (completed StateE))
				(and (equals ?s StateG)
					 (completed StateF))))
	:effect (completed ?s))
