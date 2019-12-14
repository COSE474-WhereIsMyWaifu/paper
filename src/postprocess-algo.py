predict = sorted list of BBOX
iou_threshold = merge threshold for bbox

pred_result = []
for bbox in predict:
    new_group = True
    max_matching_group = 0
    max_iou = 0
                    
    for group in pred_result:
        iou_match = iou(bbox, mean(group))
            if iou_match > iou_threshold:
                new_group = False
                if max_iou < iou_match:
                    max_iou = iou_match
                    max_matching_group = group
                                
    if new_group is True:
        new_group = make_new_group_with(bbox)
        pred_result = pred_result U new_group
    else:
        max_matching_group = max_matching_group U bbox
                        
return pred_result
