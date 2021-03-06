# later: types of translations:
# - directly linked to this view
# - directly linked to any child of this view
# - directly linked to any view that one of those views calls
# trans_obj = self.pool['ir.translation']
domain = [('type', '=', 'view')]
ctx = {'search_default_group_by_src': 1}

if object.type == "qweb":
	domain.append(('res_id', '=', object.id))
	ctx.update({
		'default_name': 'website',
		'default_res_id': object.id,
		'default_type': 'view'
		})
else:
	domain.append(('name', '=', object.model))

act_window_obj = self.pool['ir.actions.act_window']
view_action = act_window_obj.for_xml_id(cr, uid, 'base', 'action_translation', context=context)
view_action.update({
	'domain': domain,
	'context': ctx
	})
action = view_action
