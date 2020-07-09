import csv

def generate_html(csv_file):
    templates = []
    with open(csv_file) as f:
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
            year = row[4]
            template = f"""
                <tr><td><a href={href}>{paper_name}</td>
                    <td>{publish}</td>
                    <td>{comments}</td>
                    <td>{year}</td>
                </tr>
            """
            templates.append(template)
    return ''.join(templates)

survey = generate_html('survey.csv')
data_preparation = generate_html('dp.csv')
feature_engineering = generate_html('fe.csv')
nas = generate_html('nas.csv')
other = generate_html('other.csv')

full_page = """
<!DOCTYPE html><html><head><meta charset="utf-8"/><meta http-equiv="X-UA-Compatible"content="IE=edge"><title>AutoML</title><meta name="viewport"content="width=device-width, initial-scale=1"><link rel="stylesheet"type="text/css"media="screen"href="main.css"/><link rel="stylesheet"href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script><script src="index.js"></script></head><body><div class="container"id='test'><div class="row"><div class="col-md-12"><div class="panel-group"id="accordion"><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"><a data-toggle="collapse"data-parent="#accordion"href="#collapseOne">Survey</a></h4></div><div id="collapseOne"class="panel-collapse collapse in"><div class="panel-body"><table class="table table-hover table-bordered"><thead><tr><td>Paper</td><td>Published</td><td>Comments</td><td>Year</td></tr></thead><tbody>%s</tbody></table></div></div></div><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"><a data-toggle="collapse"data-parent="#accordion"href="#collapseTwo">Data Preparation</a></h4></div><div id="collapseTwo"class="panel-collapse collapse"><div class="panel-body"><table class="table table-hover table-bordered"><thead><tr><td>Paper</td><td>Published</td><td>Comments</td><td>Year</td></tr></thead><tbody>%s</tbody></table></div></div></div><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"><a data-toggle="collapse"data-parent="#accordion"href="#collapseThree">Feature Engineering</a></h4></div><div id="collapseThree"class="panel-collapse collapse"><div class="panel-body"><table class="table table-hover table-bordered"><thead><tr><td>Paper</td><td>Published</td><td>Comments</td><td>Year</td></tr></thead><tbody>%s</tbody></table></div></div></div><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"><a data-toggle="collapse"data-parent="#accordion"href="#collapseFour">Neural Architecture Search(NAS)</a></h4></div><div id="collapseFour"class="panel-collapse collapse"><div class="panel-body"><table class="table table-hover table-bordered"><thead><tr><td>Paper</td><td>Published</td><td>Comments</td><td>Year</td></tr></thead><tbody>%s</tbody></table></div></div></div><div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"><a data-toggle="collapse"data-parent="#accordion"href="#collapseFive">Others</a></h4></div><div id="collapseFive"class="panel-collapse collapse"><div class="panel-body"><table class="table table-hover table-bordered"><thead><tr><td>Paper</td><td>Published</td><td>Comments</td><td>Year</td></tr></thead><tbody>%s</tbody></table></div></div></div></div></div></div></div><script>function setHeight(){var h=document.body.clientHeight;window.parent.test(h)}setHeight();window.onresize=function(){setHeight()}document.getElementById("test").onclick=function(){this.style.height="500px";setHeight()}</script><div style="clear:both;"></div></body></html>
"""%(survey, 
    data_preparation, 
    feature_engineering,
    nas,
    other)

with open('../docs/papers.html', 'w') as f:
    f.write(full_page)
    print('Generate papers.html...\nDone.')