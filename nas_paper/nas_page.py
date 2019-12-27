import csv




# model structure


# hyperparameter optimization

# model estimation

# application


def generate_html(csv_file, data_parent, data_level):
    templates = []
    with open(csv_file, encoding='utf-8') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        rows = []
        for row in f_csv:
            rows.append(row)
        for row in sorted(rows, key=lambda x:int(x[-1]), reverse=True):
            paper_name = row[0]
            if row[1].strip()!='-':
                href = f""" "{row[1]}" target="_blank" """
            else:
                href = """ "javascript:void(0)" style="color:black;text-decoration:none;cursor:text;"  """
            
            publish = row[2]
            comments = row[3]
            year = row[-1]
            template = f'''<tr data-parent={data_parent} data-level={data_level}>
                    <td><a href={href}>{paper_name}</a></td>
                    <td>{publish}</td>
                    <td>{comments}</td>
                    <td>{year}</td>
                </tr>'''
            templates.append(template)
    return ''.join(templates)

model_structure = generate_html('nas_mg_structure.csv',"11", "3")
hyp_opt = generate_html('nas_mg_hyp.csv',"12", "3")
model_estimation = generate_html('nas_me.csv',"2", "2")
application = generate_html('nas_app.csv',"3", "2")

full_page = """
<!DOCTYPE html><html><head><meta charset="utf-8"/><meta http-equiv="X-UA-Compatible"content="IE=edge"><title>AutoML</title><meta name="viewport"content="width=device-width, initial-scale=1"><link rel="stylesheet"type="text/css"media="screen"href="main.css"/><link rel="stylesheet"href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script><style>.treegrid-indent{width:0px;height:16px;display:inline-block;position:relative}.treegrid-expander{width:0px;height:16px;display:inline-block;position:relative;left:-17px;cursor:pointer}</style></head><body><div class="container"id='test'><div class="row"><div class="col-md-12"><table id="tree-table"class="table table-hover table-bordered"><th>Paper</th><th>Publish</th><th>Comments</th><th>Year</th><tbody><!--Model Generation--><tr data-id="1"data-parent="0"data-level="1"><td data-column="name"colspan="4">Model Generation</td></tr><!--Model Structure--><tr data-id="11"data-parent="1"data-level="2"><td data-column="name"colspan="4">Model Structure</td></tr>%s<!--Hyperparameter Optimization--><tr data-id="12"data-parent="1"data-level="2"><td data-column="name"colspan="4">Hyperparameter Optimization</td></tr>%s<!--Model Estimation--><tr data-id="2"data-parent="0"data-level="1"><td data-column="name"colspan="4">Model Estimation</td></tr>%s<!--Applications--><tr data-id="3"data-parent="0"data-level="1"><td data-column="name"colspan="4">Applications</td></tr>%s</tbody></table></div></div></div><script>function setHeight(){var h=document.body.clientHeight;window.parent.test(h)}setHeight();window.onresize=function(){setHeight()}document.getElementById("test").onclick=function(){this.style.height="500px";setHeight()}</script><script src="http://code.jquery.com/jquery-1.12.4.min.js"></script><script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script><script src="js/javascript.js"></script><div style="clear:both;"></div></body></html>
"""%(model_structure, 
    hyp_opt,
    model_estimation,
    application)

with open('../docs/nas_category.html', 'w', encoding='utf-8') as f:
    f.write(full_page)