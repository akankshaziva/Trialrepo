import jenkins.model.Jenkins
name = "test_master_builder_project"
//If we want to add more then one job
def items = new LinkedHashSet();
def job = Hudson.instance.getJob(name)
items.add(job);
items.each { item ->
    try {
        def job_data = Jenkins.instance.getItemByFullName(item.fullName)
        println 'Job: ' + item.fullName
        if (job_data.getLastBuild()) {
            last_job_num = job_data.getLastBuild().getNumber()
            def upStreamBuild = Jenkins.getInstance().getItemByFullName(item.fullName).getBuildByNumber(last_job_num)
println 'LastBuildNumer: ' + last_job_num
            println "LastBuildTime: ${upStreamBuild.getTime()}"
        } else {
            println 'LastBuildNumer: Null'
        }
    } catch (Exception e) {
        println ' Ignoring exception ' + e
    }
}
